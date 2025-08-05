import sys
sys.stdin = open('input.txt')


def dfs(ori, ch_num):
    global max_num

    if ch_num == change:
        max_num = max(int(ori), max_num)
        return
    # 교환횟수가 최종 목표치와 동일 한경우 교환을 더이상 진행하지 않고 최댓값과 비교 진행

    if (ori, ch_num) in visited:
        return
    visited.add((ori, ch_num))
    # 숫자와 교환횟수가 모두 일치하는 경우 continue

    ori = list(ori)
    # 문자열에 list를 적용하여 분리
    # 밑에 로직에서 인덱싱 기반 교환이 가능하기 위하여

    for i in range(len(ori)):
        for j in range(i + 1, len(ori)):
            ori[i], ori[j] = ori[j], ori[i]
            dfs(''.join(ori), ch_num + 1)
            ori[i], ori[j] = ori[j], ori[i]
    # 전수조사 실시 : 전체 숫자를 서로 한번씩 교환한후 그 값을 dfs에 다시 전달(교환횟수 +1)
    # dfs에 값을 전달 후에도 중첩 for문을 통해 남은 값 교환을 진행해야 하기에 ori는 원상 복구를 해야함


test = int(input())
for tc in range(1, test + 1):
    origin, change = input().split()
    change = int(change)
    max_num = 0
    visited = set()
    dfs(origin, 0)
    print(f"#{tc} {max_num}")