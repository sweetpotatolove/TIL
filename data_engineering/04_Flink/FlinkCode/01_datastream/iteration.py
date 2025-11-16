from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

# 데이터에 map 연산(각 값을 2배) 수행 후 결과 반환하는 함수
def run_flink_job(input_data):
    env = StreamExecutionEnvironment.get_execution_environment()
    ds = env.from_collection(input_data, type_info=Types.INT())

    # 간단히 각 값을 2배로 변환
    mapped_ds = ds.map(lambda x: x * 2, output_type=Types.INT())

    # Flink 작업 실행
    env.execute("Driver-based iteration job")

    # 실행 후 결과 수집
    result = list(mapped_ds.execute_and_collect())
    return result

# 초기 데이터
data = [10]

# 드라이버 측에서 반복 실행
while True:
    data = run_flink_job(data)
    print("중간 결과:", data)

    # 예: 모든 값이 100 이상이면 반복 종료
    if all(x >= 100 for x in data):
        break

print("최종 결과:", data)
