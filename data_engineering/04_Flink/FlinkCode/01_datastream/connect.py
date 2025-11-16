from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types
from pyflink.datastream.functions import CoMapFunction

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()

# 서로 다른 타입의 두 스트림 입력
stream_str = env.from_collection(["A", "B"], type_info=Types.STRING())
stream_int = env.from_collection([1, 2], type_info=Types.INT())

# connect: 두 스트림을 연결
connected_stream = stream_str.connect(stream_int)

# 각 스트림에 다른 방식 처리
class MyCoMapFunction(CoMapFunction):
    def map1(self, value):
        return f"String: {value}"

    def map2(self, value):
        return f"Int: {value}"

# 연결된 스트림에 CoMapFunction 적용
co_mapped_stream = connected_stream.map(MyCoMapFunction(), output_type=Types.STRING())

# 결과 수집
result_connect = list(co_mapped_stream.execute_and_collect())
print("Connect 결과:", result_connect)
