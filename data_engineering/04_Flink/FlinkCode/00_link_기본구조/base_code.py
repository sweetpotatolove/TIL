from pyflink.datastream import StreamExecutionEnvironment

# 1. 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# 2. 데이터 소스 정의 (리스트 데이터를 스트림으로 변환)
data_stream = env.from_collection([1, 2, 3, 4, 5])

# 3. 데이터 변환 (각 숫자에 *2 연산 수행)
transformed_stream = data_stream.map(lambda x: x * 2)

# 4. 결과를 콘솔에 출력
transformed_stream.print()

# 5. 작업 실행
env.execute("Simple Flink Job")