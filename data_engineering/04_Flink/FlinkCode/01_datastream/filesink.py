from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FileSink
from pyflink.common.serialization import Encoder
from pyflink.common.typeinfo import Types
from pyflink.java_gateway import get_gateway

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()

# 데이터 소스 생성
data = ["Hello", "Flink", "World"]
data_stream = env.from_collection(data, type_info=Types.STRING())

# Java Encoder 생성
gateway = get_gateway()
j_string_encoder = gateway.jvm.org.apache.flink.api.common.serialization.SimpleStringEncoder()

# Python Encoder 생성
encoder = Encoder(j_string_encoder)

# FileSink 설정
file_sink = FileSink.for_row_format(
    "./output/result",  # 출력 디렉터리
    encoder
).build()

# Sink에 데이터 연결
data_stream.sink_to(file_sink)

# 플링크 작업 실행
env.execute("File Sink Example")
