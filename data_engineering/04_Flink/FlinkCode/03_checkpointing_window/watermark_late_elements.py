from datetime import datetime, timedelta

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import ProcessFunction
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common.typeinfo import Types
from pyflink.common.time import Time, Duration
from pyflink.common.watermark_strategy import WatermarkStrategy, TimestampAssigner


# 사용자 정의 TimestampAssigner (두 번째 필드를 타임스탬프로 사용)
class CustomTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, element, record_timestamp):
        return element[1]

# ProcessFunction: 각 이벤트와 현재 워터마크를 출력
class PrintWatermarkProcessFunction(ProcessFunction):
    def process_element(self, value, ctx):
        watermark = ctx.timer_service().current_watermark()
        print(f"Event: {value}, Current Watermark: {watermark}")
        yield value

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# 현재 시간 기준 샘플 데이터 생성 (타임스탬프: 밀리초 단위)
now = datetime.now()
data = [
    (1, int(now.timestamp() * 1000)),
    (2, int((now + timedelta(milliseconds=1000)).timestamp() * 1000)),
    (3, int((now + timedelta(milliseconds=2000)).timestamp() * 1000)),
    (4, int((now + timedelta(milliseconds=3000)).timestamp() * 1000)),
    (5, int((now + timedelta(milliseconds=4000)).timestamp() * 1000)),
]

# 데이터 소스 정의
source = env.from_collection(
    data,
    type_info=Types.TUPLE([Types.INT(), Types.LONG()])
)

# 워터마크 전략 설정: 최대 1초의 지연 허용
watermark_strategy = (
    WatermarkStrategy
        .for_bounded_out_of_orderness(Duration.of_seconds(1))
        .with_timestamp_assigner(CustomTimestampAssigner())
)

# 타임스탬프 및 워터마크 적용
watermarked_stream = source.assign_timestamps_and_watermarks(watermark_strategy)

# 이벤트와 워터마크 출력용 프로세스 스트림 (디버깅 용도)
processed_stream = watermarked_stream.process(PrintWatermarkProcessFunction())
processed_stream.print()

# 텀블링 이벤트 시간 윈도우 + allowed lateness 적용
windowed_stream = (
    watermarked_stream
        .key_by(lambda x: x[0])
        .window(TumblingEventTimeWindows.of(Time.seconds(2)))
        .allowed_lateness(Duration.of_seconds(2))
)

# 실행
env.execute("Watermark with Allowed Lateness Example")
