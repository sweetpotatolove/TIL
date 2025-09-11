import sys

sys.stdin = open('input.txt')


def process_finished_tasks(time, desks, is_repair):
    '''
        창구에서 완료된 작업을 처리합
        정비 창구의 경우 완료된 고객 수를 반환
    '''
    finished_customers_count = 0  # 이번 시간에 완료된 고객 수
    newly_waiting_customers = []  # 접수를 마치고 정비를 기다리는 고객 목록

    for i in range(len(desks)):
        if desks[i][0] > 0 and desks[i][1] == time:  # 현재 시간에 작업이 끝나는 고객이 있다면
            customer_id = desks[i][0]
            desks[i][0] = 0  # 창구 비우기
            if is_repair:
                finished_customers_count += 1  # 정비 완료 고객 수 증가
            else:
                newly_waiting_customers.append(customer_id)  # 정비 대기 큐로 이동할 고객 추가

    if is_repair:
        return finished_customers_count
    return newly_waiting_customers


def process_new_arrivals(time, all_arrival_times, arrived_idx, total_customers):
    '''
        현재 시간에 도착한 신규 고객을 처리
    '''
    newly_arrived_customers = []  # 이번 시간에 도착한 고객 목록
    while arrived_idx < total_customers and all_arrival_times[arrived_idx] == time:
        newly_arrived_customers.append(arrived_idx + 1)  # 고객 번호는 1부터 시작
        arrived_idx += 1  # 다음 도착 고객을 가리키도록 인덱스 증가
    return newly_arrived_customers, arrived_idx


def assign_customers_to_desks(time, queue, desks, processing_times, customer_log, is_repair):
    '''
        대기 큐의 고객을 빈 창구에 배정
    '''
    if not queue:  # 대기열에 고객이 없으면 종료
        return

    # 우선순위에 따라 대기 큐 정렬
    if is_repair:
        queue.sort(key=lambda cid: (customer_log[cid][1], customer_log[cid][0]))  # 정비 큐: 접수완료시간 -> 접수창구 순
    else:
        queue.sort()  # 접수 큐: 고객번호 순

    remaining_customers_in_queue = []  # 창구를 배정받지 못한 고객 목록
    for customer_id in queue:
        assigned = False
        for i in range(len(desks)):  # 번호가 낮은 창구부터 확인
            if desks[i][0] == 0:
                desks[i][0] = customer_id  # 창구에 고객 배정
                desks[i][1] = time + processing_times[i]  # 종료 시간 계산
                if is_repair:
                    customer_log[customer_id][2] = i + 1  # 정비 창구 이용 내역 기록
                else:
                    customer_log[customer_id][0] = i + 1  # 접수 창구 이용 내역 기록
                    customer_log[customer_id][1] = desks[i][1]  # 접수 완료 시간 기록
                assigned = True
                break
        if not assigned:
            remaining_customers_in_queue.append(customer_id)  # 빈 창구가 없어 대기해야 하는 고객

    # 대기 큐를 배정받지 못한 고객들로 갱신
    queue[:] = remaining_customers_in_queue


def calculate_result(total_customers, target_reception, target_repair, customer_log):
    '''
        목표 창구를 이용한 고객들의 번호 합을 계산
    '''
    total_sum = 0
    for i in range(1, total_customers + 1):
        if customer_log[i][0] == target_reception and customer_log[i][2] == target_repair:
            total_sum += i  # 조건에 맞는 고객 번호 합산

    return total_sum if total_sum > 0 else -1  # 합산 결과가 0이면 -1을 반환


def solve():
    n, m, k, A, B = map(int, input().split())  # 접수창구 수, 정비창구 수, 고객 수, 목표 창구 번호
    a = list(map(int, input().split()))  # 접수 창구별 처리 시간
    b = list(map(int, input().split()))  # 정비 창구별 처리 시간
    t = list(map(int, input().split()))  # 고객별 도착 시간

    reception_desks = [[0, 0] for _ in range(n)]  # 접수 창구 상태: [고객번호, 종료시간]
    repair_desks = [[0, 0] for _ in range(m)]  # 정비 창구 상태: [고객번호, 종료시간]
    customer_log = [[0, 0, 0] for _ in range(k + 1)]  # 고객별 이용 기록: [접수창구, 접수완료시간, 정비창구]

    reception_q = []  # 접수 대기 큐
    repair_q = []  # 정비 대기 큐

    time = 0
    finished_count = 0  # 정비를 모두 마친 고객 수
    arrived_idx = 0  # 도착 처리가 완료된 고객 인덱스

    while finished_count < k:  # 모든 고객이 정비를 마칠 때까지 시뮬레이션
        # 1. 정비 창구 완료 처리
        finished_count += process_finished_tasks(time, repair_desks, is_repair=True)
        # 2. 접수 창구 완료 처리 및 정비 큐로 이동
        repair_q.extend(process_finished_tasks(time, reception_desks, is_repair=False))
        # 3. 신규 고객 도착 처리
        new_arrivals, arrived_idx = process_new_arrivals(time, t, arrived_idx, k)
        reception_q.extend(new_arrivals)
        # 4. 정비 창구 배정
        assign_customers_to_desks(time, repair_q, repair_desks, b, customer_log, is_repair=True)
        # 5. 접수 창구 배정
        assign_customers_to_desks(time, reception_q, reception_desks, a, customer_log, is_repair=False)

        time += 1  # 시간 증가

    return calculate_result(k, A, B, customer_log)  # 최종 결과 계산 후 반환


T = int(input())
for tc in range(1, 1 + T):
    result = solve()
    print(f'#{tc} {result}')