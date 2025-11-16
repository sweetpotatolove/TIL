from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)  # 병렬 처리 방지 (출력 순서 보기 좋게)

# (무게, 주소, 냉장 여부)
data = [
    (25, "서울 강남구", False),
    (15, "강원도 산간 지역", False),
    (10, "부산 해운대", True),
    (5, "서울 관악구", False)
]

# DataStream 생성
ds = env.from_collection(
    data,
    type_info=Types.TUPLE([Types.INT(), Types.STRING(), Types.BOOLEAN()])
)

# 라벨 기반 분기 처리 (split/select 대체)
heavy = ds.filter(lambda x: x[0] > 20)
remote = ds.filter(lambda x: "산간" in x[1])
cold = ds.filter(lambda x: x[2])
normal = ds.filter(lambda x: not (x[0] > 20 or "산간" in x[1] or x[2]))

# 출력
heavy.map(lambda x: f"[무거운 택배] {x}").print()
remote.map(lambda x: f"[산간 택배] {x}").print()
cold.map(lambda x: f"[냉장 택배] {x}").print()
normal.map(lambda x: f"[일반 택배] {x}").print()

# 작업 실행
env.execute("택배 분기 처리")
