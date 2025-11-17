from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import GlobalWindows, Trigger, TriggerResult
from pyflink.datastream.state import ValueStateDescriptor
from pyflink.common.typeinfo import Types

# 사용자 정의 CountTrigger 클래스: 요소가 일정 개수에 도달하면 트리거
class CustomCountTrigger(Trigger):
    def __init__(self, count_threshold):
        super().__init__()
        self.count_threshold = count_threshold  # 몇 개마다 트리거를 실행할지 설정

    @staticmethod
    def of(count_threshold):
        return CustomCountTrigger(count_threshold)

    def on_element(self, element, timestamp, window, ctx):
        """ 새 요소가 들어올 때마다 호출됨 """
        count_state_desc = ValueStateDescriptor("count", Types.INT())  # 상태 저장용 디스크립터
        count_state = ctx.get_partitioned_state(count_state_desc)

        current_count = count_state.value() or 0
        current_count += 1
        count_state.update(current_count)

        if current_count >= self.count_threshold:
            count_state.clear()  # 카운트 리셋
            return TriggerResult.FIRE_AND_PURGE  # 트리거 실행 + 윈도우 초기화
        return TriggerResult.CONTINUE  # 계속 대기

    def on_processing_time(self, time, window, ctx):
        """ 처리 시간 기반 트리거 (사용하지 않음) """
        return TriggerResult.CONTINUE

    def on_event_time(self, time, window, ctx):
        """ 이벤트 시간 기반 트리거 (사용하지 않음) """
        return TriggerResult.CONTINUE

    def on_merge(self, window, ctx):
        """ 여러 윈도우가 병합될 때 호출됨 (사용하지 않음) """
        return TriggerResult.CONTINUE

    def clear(self, window, ctx):
        """ 윈도우가 닫힐 때 상태 초기화 """
        count_state_desc = ValueStateDescriptor("count", Types.INT())
        ctx.get_partitioned_state(count_state_desc).clear()

# 실행 환경 설정
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# 입력 데이터: 1부터 15까지의 숫자
data = [(i,) for i in range(1, 16)]
ds = env.from_collection(collection=data, type_info=Types.TUPLE([Types.INT()]))

# GlobalWindow + 사용자 정의 CountTrigger(5개마다 실행)
windowed = (
    ds.window_all(GlobalWindows.create())
      .trigger(CustomCountTrigger.of(5))
      .reduce(lambda a, b: (a[0] + b[0],))  # 집계: 합계 구하기
)

# 결과 출력
windowed.print()

# 실행
env.execute("Custom CountTrigger Example")
