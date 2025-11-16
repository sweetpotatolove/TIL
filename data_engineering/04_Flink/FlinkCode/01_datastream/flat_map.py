from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

env = StreamExecutionEnvironment.get_execution_environment()

# 문자열 리스트
input_data = ["hello", "hi"]

# DataStream 생성
ds = env.from_collection(collection=input_data, type_info=Types.STRING())

# flat_map 함수: 각 문자열을 문자 단위로 분해
def split_string(s):
    for ch in s:
        yield ch

flat_mapped_stream = ds.flat_map(split_string, output_type=Types.STRING())

# 실행 후 결과 수집
env.execute("FlatMap Job")
flat_mapped_result = list(flat_mapped_stream.execute_and_collect())

print("flat_map 결과:", flat_mapped_result)
