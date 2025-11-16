from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()

# 두 개의 정수 리스트 스트림
stream1 = env.from_collection([1, 2, 3], type_info=Types.INT())
stream2 = env.from_collection([4, 5, 6], type_info=Types.INT())

# union: 두 스트림을 하나로 결합
union_stream = stream1.union(stream2)

# 결과 수집
result_union = list(union_stream.execute_and_collect())
print("Union 결과:", result_union)
