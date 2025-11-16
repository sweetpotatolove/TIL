from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

env = StreamExecutionEnvironment.get_execution_environment()

# 정수 리스트
input_data = [1, 2, 3, 4, 5, 6]

# DataStream 생성
ds = env.from_collection(collection=input_data, type_info=Types.INT())

# filter 함수: 짝수만 통과시키기
filtered_stream = ds.filter(lambda x: x % 2 == 0)

# 실행 후 결과 수집
env.execute("Filter Job")
filtered_result = list(filtered_stream.execute_and_collect())

print("filter 결과:", filtered_result)
