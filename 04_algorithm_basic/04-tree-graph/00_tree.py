'''
아래와 같은 이진 트리가 있다면,
        'A'
       /   \
    'B'     'C'
    /  
  'D'
  /
'E'
'''
# 1번 index를 root로 설정하였을 때,
# 'A'의 왼쪽, 오른쪽 자식은 각각 2, 3 index에 해당함
# 'B'의 왼쪽, 오른쪽 자식은 각각 4, 5 index에 해당함
# 'D'의 왼쪽, 오른쪽 자식은? 

# 위 이진트리를 리스트로 나타낸다면
#        0     1    2    3    4    5     6     7    8
tree = [None, 'A', 'B', 'C', 'D', None, None, None, 'E', None, None, None, None, None, None, None]
# 계산하기 편하게 루트 노드를 index 1부터 배치
# 값이 없는 노드 자리에 None 넣어야 나머지 자식 노드들의 순서가 맞음
# 15번까지 None 삽입
# 비선형 자료구조 tree를 선형 자료구조?인 리스트로 표현


print('존재하는 모든 요소 출력하기')
# root 노드를 기준으로, 모든 존재하는 자식들의 정보를 출력해야 함
for index in range(1, 2**4):
    if tree[index]:
        print(tree[index])

print('부모 찾기')
# 'E' 노드를 기준으로, 조상 노드를 찾으로 가자
index = 8
# 2진 트리에서 부모는, 내 인덱스를 2로 나눈 몫이면 부모
while index > 1:
    parent = tree[index // 2]
    print(parent, end=' ')
    index //= 2

print()
print('왼쪽 or 오른쪽 자식 찾기')
index = 1
while index < 8:
    #  왼쪽 자식은 내 인덱스 * 2
    # 오른쪽 자식은 내 인덱스 * 2 + 1
    left_child = tree[index * 2]
    right_child = tree[index * 2 + 1]
    print(left_child)
    print(right_child)
    index *= 2

