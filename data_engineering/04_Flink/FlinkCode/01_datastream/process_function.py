from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import ProcessFunction
from pyflink.common.typeinfo import Types

# ProcessFunction 예제: 짝수면 2배, 홀수면 그대로 반환
class MyProcessFunction(ProcessFunction):
    def process_element(self, value, ctx: 'ProcessFunction.Context'):
        if value % 2 == 0:
            yield value * 2  # 짝수이면 2배로 출력
        else:
            yield value       # 홀수이면 그대로 출력

# 실행 환경 생성 및 병렬도 설정
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# 정수 리스트
data = [1, 2, 3, 4, 5, 6]

# DataStream 생성
ds = env.from_collection(collection=data, type_info=Types.INT())

# ProcessFunction 적용 (결과 타입 명시)
processed_stream = ds.process(MyProcessFunction(), output_type=Types.INT())

# Flink 작업 실행
env.execute("ProcessFunction Example")

# 실행 후 결과 수집
result = list(processed_stream.execute_and_collect())
print("Process function result:", result)
