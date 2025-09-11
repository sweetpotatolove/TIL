import sys
sys.stdin = open('input.txt')


def BFS(S):
    # 탐색 시작 노드, 누적 탐색 횟수
    q = [(S, 0)]
    while q:
        s, cnt = q.pop(0)
        for i in G.get(s, []):          # S의 인접 리스트를 순회
            if not visited[i]:          # 아직 방문 한 적 없다면
                visited[i] = cnt+1      # 도착까지 걸린 시간 해당 학생 번호에 기록
                q.append((i, cnt+1))    # 다음 조사
    # 마지막 조사 대상 반환
    return s



for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    # 방문 표시 - index는 학생 번호
    visited = [0] * 101
    G = {}  # 인접행렬 정보 기록용 dict
    for i in range(N//2):
        # from을 key로, to를 val로
        G[arr[i*2]] = G.get(arr[i*2], []) + [arr[i*2+1]]

    # S 부터 탐색 시작
    last = BFS(S)   # 가장 마지막에 조사하긴 했지만,
    # 가장 수가 높은지는 알 수 없으므로
    # 뒷 번호 부터, 마지막 조사 대상과 같은 값을 가진 번호 조회
    for i in range(len(visited)-1, -1, -1):
        if visited[i] == visited[last]:
            # 출력 후 종료
            print(f'#{tc} {i}')
            break