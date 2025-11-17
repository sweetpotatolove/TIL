import pandas as pd
import time

from pyflink.datastream import StreamExecutionEnvironment, KeyedProcessFunction
from pyflink.datastream.checkpoint_config import CheckpointConfig
from pyflink.datastream.checkpoint_storage import FileSystemCheckpointStorage
from pyflink.datastream.state import ValueStateDescriptor
from pyflink.common.typeinfo import Types


# 상태 기반 연산 정의
class KeyedSum(KeyedProcessFunction):

    def __init__(self):
        self.state = None

    def open(self, runtime_context):
        descriptor = ValueStateDescriptor("sum", Types.FLOAT())
        self.state = runtime_context.get_state(descriptor)
        
    # ctx는 타이머/워터마크용 컨텍스트지만 이 예제에서는 사용하지 않음
    def process_element(self, value, ctx):
        current_sum = self.state.value() or 0.0
        new_sum = current_sum + value[1]
        self.state.update(new_sum)

        print(f"[{value[0]}] 누적 금액: {new_sum}")

        yield (value[0], new_sum)

# 실행 환경 설정
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# Checkpoint 설정
env.enable_checkpointing(10000)  # 10초 간격
env.get_checkpoint_config().set_checkpoint_storage(
    FileSystemCheckpointStorage("file:///home/ssafy/flink_checkpointing/flink-checkpoints")
)

# CSV 데이터 로드
df = pd.read_csv("data.csv")
base_data = df[["transaction_id", "amount"]].dropna().values.tolist()

# Job이 너무 빨리 끝나지 않게 데이터 좀 늘리기
transactions = base_data * 100000  # 필요하면 숫자 더 줄여도 됨

# Flink 데이터 스트림 생성
transaction_stream = env.from_collection(
    transactions,
    type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()])
)

# 상태 연산 적용 + output_type 명시
result_stream = (
    transaction_stream
        .key_by(lambda x: x[0])
        .process(
            KeyedSum(),
            output_type=Types.TUPLE([Types.STRING(), Types.FLOAT()])
        )
)

# Sink
result_stream.print()

# 실행
env.execute("Checkpointing Example")

'''
PyFlink에서 Checkpoint 디렉토리에 _metadata 파일만 생성되고,
우리가 기대하는 state가 담긴 실제 파일이 보이지 않는 이유는
상태(state)를 저장하는 책임이 Python이 아니라 JVM(Java) 레이어의 State Backend에 있기 때문입니다.

PyFlink 코드에서 ValueState나 KeyedState를 업데이트하면,
이 상태는 Python 프로세스가 직접 파일로 쓰지 않고,
Python → Java 연동 레이어를 거쳐 Java Operator가 관리하는 State Backend에 저장됩니다.

여기서 중요한 점은 Flink의 기본 State Backend(HashMapStateBackend 또는 MemoryStateBackend)는
상태 용량이 매우 작은 경우 별도의 파일로 분리하지 않고,
checkpoint 메타데이터 파일(_metadata) 안에 'inline' 형태로 저장한다는 것입니다.

따라서 KeyedState(ValueState)가 float 하나처럼 매우 작은 상태일 경우,
checkpoint 디렉토리에는 _metadata 파일만 생성되고,
실제 상태를 담은 별도 파일(shared, private 등)은 생성되지 않습니다.
이는 정상 동작입니다.

요약:
- PyFlink의 state 저장은 Python이 아닌 Java State Backend가 담당한다.
- 작은 state는 checkpoint 디렉토리에 개별 state 파일로 저장되지 않고 _metadata 안에 포함된다.
- 따라서 _metadata 파일만 보이는 것은 정상이며, 오류가 아니다.
- RocksDBStateBackend를 사용하면 state가 별도 파일로 생성되는 것을 확인할 수 있다.
'''