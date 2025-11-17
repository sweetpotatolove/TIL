import time
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import SlidingProcessingTimeWindows
from pyflink.common.time import Time
from pyflink.common.typeinfo import Types

# 각 이벤트별 지연 시간을 설정하는 함수
# record: (user, value)
def delayed_map(record):
    if record[1] == 0:
        time.sleep(5)
    elif record[1] in [1, 3]:
        time.sleep(0.5)
    elif record[1] == 4:
        time.sleep(2.8)
    elif record[1] == 5:
        time.sleep(0.5)
    return record

# 실행 환경 생성 및 병렬성 1로 설정
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# 데이터 소스 생성
data = [("user1", 1), ("user1", 3), ("user1", 4), ("user1", 5), ("user1", 0)]
data_stream = env.from_collection(
    collection=data,
    type_info=Types.TUPLE([Types.STRING(), Types.INT()])
)


# map 연산 내에서 1.2초 지연 추가 (time.sleep)
delayed_stream = data_stream.map(
    lambda x: (x[0], x[1]) if time.sleep(1.2) is None else (x[0], x[1]),
    output_type=Types.TUPLE([Types.STRING(), Types.INT()])
)

# 슬라이딩 윈도우 적용: 윈도우 크기 2초, 슬라이드 간격 1초
windowed_stream = (
    delayed_stream
        .key_by(lambda x: x[0])
        .window(SlidingProcessingTimeWindows.of(Time.seconds(2), Time.seconds(1)))
        .reduce(lambda a, b: (a[0], a[1] + b[1]))
)

windowed_stream.print()
env.execute("ProcessingTime Window Example")


'''
ProcessingTime 윈도우는 절대 신뢰할 수 없음
이벤트가 몇 초 뒤에 들어올지 알 수 없음
윈도우가 시간 기반으로 계속 닫혀버림
-> 이를 정확히 하고자 한다면 EvenvtTime 기반의 윈도우를 사용해야 함
'''