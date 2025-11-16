from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

# Flink 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()

# 예제 입력: 정수 리스트
data = env.from_collection([1, 2, 3, 4, 5, 6], type_info=Types.INT())

# filter 연산을 이용하여 조건에 맞게 데이터 스트림 분할
even_stream = data.filter(lambda x: x % 2 == 0)  # 짝수 스트림
odd_stream = data.filter(lambda x: x % 2 != 0)   # 홀수 스트림

# 작업 실행
env.execute("Split Stream Example")

# 결과 수집
evens = list(even_stream.execute_and_collect())
odds = list(odd_stream.execute_and_collect())

# 출력
print("Even stream:", evens)
print("Odd stream:", odds)
