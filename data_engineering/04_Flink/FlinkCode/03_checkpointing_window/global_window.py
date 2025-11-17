from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import GlobalWindows, Trigger, TriggerResult
from pyflink.datastream.state import ValueStateDescriptor
from pyflink.common.typeinfo import Types

# 사용자 정의 CountTrigger: 요소가 3개 모이면 FIRE_AND_PURGE
class CustomCountTrigger(Trigger):
    def __init__(self, count):
        super(CustomCountTrigger, self).__init__()
        self.count = count

    @staticmethod
    def of(count):
        return CustomCountTrigger(count)

    def on_element(self, element, timestamp, window, ctx):
        state_desc = ValueStateDescriptor("count", Types.INT())
        state = ctx.get_partitioned_state(state_desc)
        current = state.value() or 0
        current += 1
        state.update(current)

        if current >= self.count:
            state.clear()
            return TriggerResult.FIRE_AND_PURGE
        else:
            return TriggerResult.CONTINUE

    def on_processing_time(self, time, window, ctx):
        return TriggerResult.CONTINUE

    def on_event_time(self, time, window, ctx):
        return TriggerResult.CONTINUE

    def clear(self, window, ctx):
        state_desc = ValueStateDescriptor("count", Types.INT())
        ctx.get_partitioned_state(state_desc).clear()

    def on_merge(self, window, ctx):
        return TriggerResult.CONTINUE

# 실행 환경 생성
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# 입력 데이터: 정수 리스트
data = [1, 2, 3, 4, 5, 6]
ds = env.from_collection(collection=data, type_info=Types.INT())

# Global Windows 적용: 전체 스트림을 하나의 윈도우로 묶고,
# 요소 3개마다 트리거 발생 (CustomCountTrigger.of(3))
windowed = (
    ds.window_all(GlobalWindows.create())
      .trigger(CustomCountTrigger.of(3))
      .reduce(lambda a, b: a + b)
)

# 결과 출력
windowed.print()

# 애플리케이션 실행
env.execute("GlobalWindows Example")
