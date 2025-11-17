import time

# 데이터 생성 (타임스탬프 포함): 1분 단위로 과거 1시간치
data = [(i, time.time() - (i * 60)) for i in range(1, 61)]  # (1분 전 ~ 60분 전)

# Evictor 클래스 정의: 최근 N초 이내 데이터만 유지
class TimeEvictor:
    def __init__(self, max_time_seconds):
        self.max_time_seconds = max_time_seconds

    def evict_before(self, elements):
        current_time = time.time()
        
        # 유지할 데이터: 현재 시간과의 차이가 max_time_seconds 이내
        filtered = [e for e in elements if current_time - e[1] <= self.max_time_seconds]
        removed = [e for e in elements if e not in filtered]

        # 디버그 출력
        print("\n**Evictor 적용 결과**")
        print(f"* 총 입력 데이터 개수: {len(elements)}")
        print(f"* 유지된 데이터 개수 (최근 {self.max_time_seconds // 60}분): {len(filtered)}")
        print(f"* 제거된 데이터 개수: {len(removed)}")

        print("\n* 유지된 데이터 (Evictor 적용 후):")
        print(filtered)

        print("\n* 제거된 데이터:")
        print(removed)

        return filtered

# 테스트 실행 함수
def time_evictor_example():
    print("**Evictor 적용 전 전체 데이터:**")
    print(data)

    evictor = TimeEvictor(max_time_seconds=600)  # 최근 10분(600초) 유지
    result = evictor.evict_before(data)

# 함수 호출로 실행
time_evictor_example()
