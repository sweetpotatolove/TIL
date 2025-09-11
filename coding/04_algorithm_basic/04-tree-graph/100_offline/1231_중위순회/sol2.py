import sys
sys.stdin = open('input.txt')


def inorder(node):
    # 노드 번호가 0이 아니라면 조사 진행
    if node:
        inorder(data[node][2])     # 왼쪽
        print(data[node][1], end='')
        inorder(data[node][3])     # 오른쪽

for tc in range(1, 11):
    N = int(input())
    # 입력 받은 각 값이 정수라면, 정수로 아니면 문자열로 리스트에 삽입
    # map(function, iterable) -> iterable이 가진 각 요소를 첫번째 인자 function에 집어넣어서
    # 반환 값을 모으는 역할을 하는게 map
    # lambda x: 익명 함수
		# x 요소가 isdecimal 숫자라면 int(x)로 정수로 변환, 숫자가 아니라면, 입력받은 문자 그대로 유지.
    data = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    print(data)
    # 각 데이터의 길이가 상이하므로 0이 될 때까지 값 추가
    # print(data)
    for arr in data:
        while len(arr) != 4:
            arr.append(0)
    # print(data)
    # 0번 index가 없으므로 0번째 값 추가
    data.insert(0, [0, 0, 0, 0])
    # print(data)
    print(f'#{tc}', end=' ')
    # 1번 노드부터 중위 순회
    inorder(1)
    print()