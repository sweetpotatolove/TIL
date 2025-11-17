import time
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import ProcessingTimeSessionWindows
from pyflink.common.time import Time
from pyflink.common.typeinfo import Types

# 각 이벤트별 지연 시간을 설정하는 함수
# record: (user, value)
def delayed_map(record):
    # Session 테스트를 위해 데이터별 딜레이 설정.
    if record[1] == 0:
        time.sleep(5)
    elif record[1] in [1, 3]:
        time.sleep(0.5)
    elif record[1] == 4:
        time.sleep(2)
    elif record[1] == 5:
        time.sleep(0.2)
    return record

# 실행 환경 설정
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# dummy 이벤트를 포함하여 데이터를 준비
data = [("user1", 1), ("user1", 3), ("user1", 4), ("user1", 5), ("user1", 0)]
data_stream = env.from_collection(
    collection=data,
    type_info=Types.TUPLE([Types.STRING(), Types.INT()])
)

# map 연산에서 지연 적용
delayed_stream = data_stream.map(
    delayed_map,
    output_type=Types.TUPLE([Types.STRING(), Types.INT()])
)

# Processing Time Session Window: gap 2초
windowed_stream = (
    delayed_stream
        .key_by(lambda x: x[0])
        .window(ProcessingTimeSessionWindows.with_gap(Time.seconds(2)))
        .reduce(lambda a, b: (a[0], a[1] + b[1]))
)

windowed_stream.print()
env.execute("Session Window Split Example")

# 잡 실행 후 추가 대기 (출력 flush를 위해)
time.sleep(5)
