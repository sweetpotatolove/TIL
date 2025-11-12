from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()

# 병렬도 설정
env.set_parallelism(1)

# 예시 데이터 소스 생성
data = env.from_collection(
    collection=[("apple", 1), ("banana", 1), ("apple", 1)],
    type_info=Types.TUPLE([Types.STRING(), Types.INT()])
)

# transformation 적용: keyBy + sum
result = data.key_by(lambda x: x[0]) \
             .sum(1)

# DAG 실행 계획 출력 (JSON 문자열 형식)
execution_plan = env.get_execution_plan()
print("DAG Execution Plan:\n", execution_plan)

# 출력: 콘솔에 출력
result.print()

# 실행
env.execute("Basic PyFlink Job")
