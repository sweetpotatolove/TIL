# 트리와 그래프
## 트리
상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조
- 비선형 구조
- 원소들 간에 1:N 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 한 개 이상의 노드로 이루어진 유한 집합
    - 노드 중 최상위 노드를 **루트(root)**라고 함
    - 나머지 노드들은 n (>=0)개의 분리집합 `T1, .. , Tn`으로 분리될 수 있음
- T1, .., Tn은 각각 하나의 트리가 되며, 루트의 **부 트리(subtree)**라고 함

    ![tree](tree.png)

### 트리 용어
![tree2](tree2.png)

- **노드(node)**
    - 트리의 원소
    - A, B, .., K
- **간선(edge)**
    - 노드와 노드를 연결하는 선
    - 부모 노드와 자식 노드를 연결
- **루트 노드(root node)**
    - 트리의 시작 노드인 최상위 노드
    - 트리 T의 루트 노드 - A
- 형제 노드(sibling node)
    - 같은 부모 노드의 자식 노드들
    - B, C, D는 형제 노드
- 조상 노드(ancestor node)
    - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
    - K의 조상 노드: F, B, A
- 서브 트리(subtee)
    - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드(descendant node)
    - 서브 트리에 있는 하위 레벨의 노드들
    - B의 자손 노드: E, F, K
- 차수(degree)
    - 노드의 차수
        - 노드에 연결된 자식 노드 수
        - B의 차수 = 2, C의 차수 = 1
    - 트리의 차수
        - 트리에 있는 노드의 차수 중 가장 큰 값
        - 트리 T의 차수 = 3
    - 단말 노드(leaf node)
        - 차수가 0인 노드 즉, 자식 노드가 없는 노드
- 레벨
    - 루트에서 노드까지의 거리
    - 루트 노드의 레벨은 0, 자식 노드의 레벨은 부모 레벨 + 1

        ![트리 레벨](트리레벨.png)
- 높이
    - 루트 노드에서 가장 먼 리프 노드까지의 간선 수
    - 트리의 높이는 최대 레벨(트리 T의 높이 = 3)


### 이진 트리(Binary Tree)
각 노드가 자식 노드를 최대한 2개까지만 가질 수 있는 트리(왼쪽/오른쪽 자식 노드)
- 차수가 2인 트리
- 모든 노드들이 최대 2개의 서브 트리를 갖는 특별한 형태의 트리
- 즉, `레벨 i에서 노드의 최대 개수는 2i`개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 `최소 개수는 h+1`개가 되고, `최대 개수는 2^(n+1)-1`개가 됨

    ![이진트리](이진트리.png)


### 포화 이진 트리(Perfect Binary Tree)
모든 레벨에 노드가 포화 상태로 차 있는 이진 트리
- 높이가 h일 때 최대 노드 개수인 `2^(h+1)-1`의 노드를 가진 이진 트리
    - 높이가 3일 때 2^(3+1)-1 = 15개의 노드
- 루트를 1번으로 하여 `2^(h+1)-1`까지 정해진 위치에 대한 노드 번호를 가짐
    
    ![포화이진트리](포화이진트리.png)


### 완전 이진 트리(complete Binary Tree)
높이가 h이고 노드 수가 n일 때 (단, h+1 <= n < 2^(h+1)-1) 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
- ex. 노드가 10개인 완전 이진 트리

    ![완전이진트리](완전이진트리.png)


### 편향 이진 트리(Skewed Binary Tree)
높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리

![편향이진트리](편향이진트리.png)


### 리스트를 이용한 이진 트리 표현
![리스트 이진 트리](리스트이진트리.png)
- 이진 트리에 각 노드 번호를 부여
- 루트 번호를 1로
- 레벨n에 있는 노드에 대해 왼쪽부터 오른쪽으로 2^n부터 2^(n+1)-1까지 차례로 부여
- 노드 번호가 i일 때
    
    ![리스트 이진 트리](리스트이진트리2.png)
    - 노드 번호를 리스트의 인덱스로 사용

- 높이가 h인 이진 트리를 위한 배열 크기
    - 레벨 i의 최대 노드 수: `2^i`
    - 따라서 모든 노드의 수: `2^(h+1)-1`
    - 그러므로 리스트 크기: `2^(h+1)`
        ![이진트리 리스트](이진트리리스트.png)

- 편향 이진 트리를 리스트로 표현한다면?
    
    ![편향 이진 트리 리스트](편향이진트리리스트.png)

- 리스트를 이용한 이진 트리 코드1 (00_tree.py)
    ```python
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

    # 위 이진트리를 리스트로 나타낸다면
    #        0     1    2    3    4    5     6     7    8
    tree = [None, 'A', 'B', 'C', 'D', None, None, None, 'E', None, None, None, None, None, None, None]
    # 계산하기 편하게 루트 노드를 index 1부터 배치
    # 값이 없는 노드 자리에 None 넣어야 나머지 자식 노드들의 순서가 맞음
    # 15번까지 None 삽입
    # 비선형 자료구조 tree를 선형 자료구조로 만들어서 사용 가능

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
    ```
- 리스트를 이용한 이진 트리 코드2 (01_make_tree.py)
    ```python
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
    ```
- 리스트를 이용한 이진 트리 코드3(02_make_tree.py)
    ```python
    # 부모의 정보만 주어질 때, 이진 트리 생성하기
    # 자신의 값, 부모 인덱스 (부모가 0인 경우, 루트)
    input_data = [
        ['A', 0],
        ['C', 1],
        ['B', 1],
        ['F', 3],
        ['G', 6],
        ['E', 2],
        ['D', 2]
    ]

    N = 16
    tree = [0] * (N+1)
    print(tree)

    for data in input_data:
        print(data)
        value = data[0]     # A
        parent = data[1]    # 0

        # 자식 인덱스 계산
        left_child = parent * 2
        right_child = parent * 2 + 1

        # 나에게 주어진 정보가 부모 노드의 index 뿐이니
        # 내가 이진 트리에서 어디에 삽입될 수 있는지를 보려면
        # 당연하게도 부모 노드의 왼, 오 자식 중 비어있는 곳을 찾아야 함

        # 내 부모가 없다 -> 0이다 -> 내가 루트 노드다
        if not parent:
            tree[1] = value     # 루트 노드 위치에 나를 삽입
            continue            # 다음 for문으로 넘김

        if not tree[left_child]:    # 왼쪽 자식이 비어있으면
            tree[left_child] = value    # 나를 삽입
        else:
            tree[right_child] = value   # 왼쪽 자식이 안비어있으면 오른쪽에 나 삽입
    print(tree)
    ```

- 편향 이진 트리의 경우 사용하지 않는 리스트 원소에 대한 메모리 공간 낭비 발생
    - 트리 중간에 새로운 노드 삽입 or 기존 노드 삭제할 경우 리스트 크기 변경이 어려워 비효율적
    - 연결 리스트 이용하자

### 연결 리스트를 이용한 이진 트리 표현
이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 이중 연결 리스트 노드를 사용하여 구현

![연결리스트 이진트리](연결리스트이진트리.png)

![완전 이진 트리 연결리스트](완전이진트리연결리스트.png)


## 이진 트리 순회(traversal)
- 순회(traversal): 트리의 노드들을 체계적으로 방문하는 것

    ![이진 트리 순회](이진트리순회.png)
- 기본적인 순회 방법 3가지
    - 전위 순회(preorder traversal): VLR
        - **부모노드** -> 자식노드(좌) -> 자식노드(우) 순서로 방문
    - 중위 순회(inorder traversal): LVR
        - 자식(좌) -> **부모** -> 자식(우) 노드 순으로 방문
    - 후위 순회(postorder traversal): LRV
        - 자식(좌) -> 자식(우) -> **부모** 노드 순으로 방문

※ 방문한다는 것은 일의 처리를 그때 처리한다는 의미

### 전위 순회
- 수행 방법
    1. 현재 노드 T를 방문하여 처리 -> V
    2. 현재 노드 T의 왼쪽 서브 트리로 이동 -> L
    3. 현재 노드 T의 오른쪽 서브 트리로 이동 -> R
- 수행 순서
    1. A -> T1 -> T2
    2. A -> **B (T3) E** -> **C F G**
    3. A B **D H I** E C F G
    ![전위순회](전위순회.png)
```python
# 리스트 구현
def preorder_traversal(idx):
    # 어디까지 순회해야 하는지?
    # 순회 대상이 범위를 벗어나지 않았다면
    if idx <= N:    # 완전 이진 트리이므로 내가 조사해야 하는 노드 개수는 N개(뒤에 더 없음)
        # 전위 순회는 부모 노드를 먼저 조사
        print(tree[idx], end=' ')
        # 이제 왼쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx * 2)
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx * 2 + 1)

tree = [0, 'A', 'B', 'C', 'D', 'E']
preorder_traversal(1)  # 'A' 'B' 'D' 'E' 'C'

# 연결리스트 구현
class TreeNode:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key  # 노드의 값

def preorder_traversal(root):
    if root:
        print(root.val)  # 현재 노드 방문
        preorder_traversal(root.left)  # 왼쪽 서브트리 방문
        preorder_traversal(root.right)  # 오른쪽 서브트리 방문
```

### 중위 순회
- 수행 방법
    1. 현재 노드 T의 왼쪽 서브 트리로 이동 -> L
    2. 현재 노드 T를 방문하여 처리 -> V 
    3. 현재 노드 T의 오른쪽 서브 트리로 이동 -> R
- 수행 순서
    1. T1 -> A -> T2
    2. **(T3) B E** -> A ->  **F C G**
    3. **H D I** B E A F C G
    ![중위순회](전위순회.png)
```python
# 리스트 구현
def inorder_traversal(idx):
    # 중위순회란, 부모 노드 차례가 중간인 순회 방식
    # 즉, 왼쪽 서브 트리에 대한 처리가 우선되어야 함

    # 전위 순회 코드에서 순서만 바꾸면 됨
    if idx <= N:
        # 왼쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2)
        # 중위 순회는 왼쪽 서브트리 순회 후 조사
        print(tree[idx], end=' ')
        # 오른쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2 + 1)

tree = [0, 'A', 'B', 'C', 'D', 'E']
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'

# 연결리스트 구현
class TreeNode:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key  # 노드의 값

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)  # 왼쪽 서브트리 방문
        print(root.val)  # 현재 노드 방문
        inorder_traversal(root.right)  # 오른쪽 서브트리 방문
```
- 리스트 구현 방식은 뭐 이진 트리6

### 후위 순회
- 수행 방법
    1. 현재 노드 T의 왼쪽 서브 트리로 이동 -> L
    2. 현재 노드 T의 오른쪽 서브 트리로 이동 -> R
    3. 현재 노드 T를 방문하여 처리 -> V 
- 수행 순서
    1. T1 -> T2 -> A
    2. **(T3) E B** -> **F G C** -> A   
    3. **H I D** E B F G C A
    ![후위순회](전위순회.png)
```python
# 리스트 구현
def postorder_traversal(idx):
    if idx <= N:
        # 왼쪽 서브 트리에 대해서도 동일한 조건
        postorder_traversal(idx * 2)
        # 오른쪽 서브 트리에 대해서도 동일한 조건
        postorder_traversal(idx * 2 + 1)
        # 후위 순회는 모든 서브트리 순회 후 조사
        print(tree[idx], end=' ')

tree = [0, 'A', 'B', 'C', 'D', 'E']
postorder_traversal(1)  # 'D' 'E' 'B' 'C' 'A'

# 연결리스트 구현
class TreeNode:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key  # 노드의 값

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)  # 왼쪽 서브트리 방문
        postorder_traversal(root.right)  # 오른쪽 서브트리 방문
        print(root.val)  # 현재 노드 방문
```

---
---
---
### 수식 트리(Expression Tree)
수식을 표현하는 이진 트리
- 수식 이진 트리(Expression binary Tree)라고 부르기도 함
- 연산자는 루트 노드이거나 가지 노드
- 피연산자는 모두 잎 노드

    ![수식트리](수식트리.png)

- 수식 트리 순회

    ![수식 트리 순회](수식트리순회.png)
    - 전위 순회: `+ * * / A B C D E`
    - 중위 순회: `A / B * C * D + E`
    - 후위 순회: `A B / C * D * E +`

- 후위 표기법이랑 다른거억

- 자식 노드는 정수인데 부모 노드는 문자열인 서브트리가 있다면?
- 문자열 서브트리를 자식으로 갖는 트리는 자식노드 임에도 불구하고 문자열
입력받는 데이터로서 전부 문자열 형태로 오게 됨 -> 연산 시 형변환 해야함
- 함수 반환값의 데이터타입 중요성


## 그래프
아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현
- 그래프는 정점(Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 자료 구조
    - V: 정점의 개수
    - E: 그래프에 포함된 간선 개수
    - V개의 정점을 가지는 `그래프는 최대 V * (V-1) / 2` 간선이 가능(암기XX)
    - ex. 5개의 정점이 있는 그래프의 최대 간선 수는 (5*4/2) = 10개
- 선형 자료구조나 트리 자료구조로 표현하기 어려운 **N:M 관계를 가지는 원소들을 표현하기에 용이**함

### 그래프 용어
- 정점(Vertax): 그래프의 구성요소로 하나의 연결점
- 간선(Edge): 두 정점을 연결하는 선
- 차수(Degree): 정점에 연결된 간선 수

### 그래프 유형
- 무방향 그래프(Undirected Graph)
    - 간선에 방향성이 존재하지 않을 때

        ![무방향그래프]()

- 방향 그래프(Directed Graph)
    - 간선에 방향성이 존재할 때

        ![방향그래프]()
        - 차수의 개념이 조금 달라짐
        - '진출차수', '진입차수'
        - 0번 노드는 2개의 진출 차수(1번, 3번), 1개의 진입 차수(1번)를 가짐

- 가중치 그래프(Weighted Graph)
    - 음냐링

        ![가중치그래프]()
        - 무방향 그래프일 때도 가중치 가능

- 사이클이 없는 방향 그래프(DAG, Direct Acyclic Graph)
    - 무방향 그래프는 언제든지 사이클 돌 수 있어서 방향 그래프에 대해서만 생각

        ![사이클이 없는 방향그래프]()

- 트리(Tree)
    - 각 노드는 최대 하나의 부모 노드가 존재할 수 있음
    - 각 노드는 자식 노드가 없거나 하나 이상 존재할 수 있음
    - 두 노드 사이에는 유일한 경로 존재


- 완전 그래프
    - 정점들에 대해 가능한 모든 간선들을 가진 그래프

- 부분 그래프
    - 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

**※ 인접(Adjacency) 정점**

