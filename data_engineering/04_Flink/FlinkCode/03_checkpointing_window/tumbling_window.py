import time
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import TumblingProcessingTimeWindows
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

# 각 요소 처리 시 지연 적용: 도착 시간을 조절
delayed_stream = data_stream.map(
    delayed_map,
    output_type=Types.TUPLE([Types.STRING(), Types.INT()])
)

# 텀블링 윈도우 적용: 2초 간격의 윈도우 (겹치지 않는 고정 윈도우)
windowed_stream = (
    delayed_stream
        .key_by(lambda x: x[0])
        .window(TumblingProcessingTimeWindows.of(Time.seconds(2)))
        .reduce(lambda a, b: (a[0], a[1] + b[1]))
)

# 윈도우 연산 결과를 콘솔에 출력
windowed_stream.print()

# 애플리케이션 실행
env.execute("Tumbling Window Example")

# 잡 실행 후 추가 대기 (출력 flush를 위해)
time.sleep(5)
