from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()

# (사용자, 값) 튜플들의 리스트
input_data = [("A", 1), ("B", 2), ("A", 3), ("B", 4)]

# DataStream 생성 (튜플 타입: (String, Int))
ds = env.from_collection(
    input_data,
    type_info=Types.TUPLE([Types.STRING(), Types.INT()])
)

# keyBy: 사용자(첫 번째 요소)를 기준으로 그룹화
keyed_stream = ds.key_by(lambda x: x[0])

# 각 키 그룹에서 값을 합산하여 변화를 확인
summed_stream = keyed_stream.reduce(lambda a, b: (a[0], a[1] + b[1]))

# 결과 출력
summed_stream.print()

# 실행
env.execute("KeyBy Visualization")
