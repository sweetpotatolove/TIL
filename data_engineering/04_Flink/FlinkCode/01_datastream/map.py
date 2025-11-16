from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

# Flink 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()

# 정수 리스트
input_data = [1, 2, 3, 4]

# DataStream 생성
ds = env.from_collection(collection=input_data, type_info=Types.INT())

# map 함수: 각 요소에 2를 곱하기
mapped_stream = ds.map(lambda x: x * 2, output_type=Types.INT())

# 실행 후 결과 수집
env.execute("Simple Map Job")  # Flink 1.20.0 이상에서는 명시적으로 호출 필요
mapped_result = list(mapped_stream.execute_and_collect())

print("map 결과:", mapped_result)
