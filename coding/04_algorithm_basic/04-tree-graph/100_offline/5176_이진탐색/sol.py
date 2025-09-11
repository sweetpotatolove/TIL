import sys
sys.stdin = open('input.txt')

# 중위 순회
# 1. index는 매개변수로 넘기면 됨
# 2. value는 어떡함?
def inorder(index):
    # 중위 순회 도중에 할당 해야 할 값을 변경해야 한다면
    # global (전역 변수로) 정의 해둔 값을 직접 변화를 시키자
    global value
    # index를 어디까지 조사할 수 있도록 처리 해야 하는가?
    # index의 역할 -> 내가 삽입 가능한 node의 번호
    # 그건 tree의 최대 크기와 같다 -> node의 index번호
    if index <= N:    # 최대 조사 가능 범위
        inorder(index * 2)  # 왼쪽 자식은 내 인덱스 * 2
        # 여기가 중위 순회의 할 일 영역인데
        tree[index] = value     # 내 위치에 value 삽입
        # 다음 값은 value가 1 증가 해야한다.
        value += 1
        inorder(index * 2 + 1)  # 오른쪽 자식은 내 인덱스 * 2 + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 0번 노드는 사용하지 않을 것이다.
    # 완전 이진트리를 만들것이기 때문에
    # node가 저장되어야 할 공간은 전체 노드의 개수만큼이면 된다.
    tree = [0] * (N+1)
    value = 1   # 첫 조사 시작시에는 1부터 삽입하기 시작할거다.
    inorder(1)
    print(tree)