# 본인 인덱스, 본인 값, 왼쪽 자식 인덱스, 오른쪽 자식 인덱스
input_data = [
    [1, 'A', 2, 3],
    [2, 'B', 4, 0],
    [3, 'C', 0, 0],
    [4, 'D', 8, 0],
    [8, 'E', 15, 0],
]

N = 16
tree = [0] * (N+1)  # 0번 노드 사용하지 않음!
print(tree)

for idx in range(len(input_data)):
    print(input_data[idx])
    my_idx = input_data[idx][0]
    value = input_data[idx][1]
    tree[my_idx] = value
print(tree)
# 보통은 입력받는 데이터가 내 위치 잘 모름
# 내 부모가 누구인지만 주어지는 경우가 일반적
# 02_make_tree2.py