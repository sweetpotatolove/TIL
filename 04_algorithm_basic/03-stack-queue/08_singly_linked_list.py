class Node:
    def __init__(self, data):
        self.data = data  # 노드의 데이터
        self.next = None  # 다음 노드를 가리키는 포인터

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # 링크드 리스트의 헤드 초기화

    # 특정 위치에 노드를 삽입하는 메서드
    def insert(self, data, position):
        pass

    # 리스트의 끝에 노드를 추가하는 메서드
    def append(self, data):
        # 삽입하려고 하는 데이터를 토대로 Node 생성
        new_node = Node(data)
        if self.is_empty():     # 비어있다면
            self.head = new_node
        else:
            current = self.head
            while current.next:             # 1번 객체의 next를 봤을 때 가리키고 있는 2번 객체가 있다면
                current = current.next      # 2번 객체를 기준으로 next 확인
            current.next = new_node         # 새로운 노드를 마지막 노드의 next가 가리킬 수 있도록..


    # 리스트가 비어있는지 확인하는 메서드
    def is_empty(self):
        return self.head is None    # 헤드가 none이니?

    # 특정 위치의 노드를 삭제하는 메서드
    def delete(self, position):
        pass

    # 특정 데이터를 가진 노드의 위치를 찾는 메서드
    def search(self, data):
        pass

    # 리스트를 문자열로 변환하는 메서드
    def __str__(self):
        result = []
        current = self.head
        while current:  # 리스트를 순회하며 데이터를 결과 리스트에 추가
            result.append(current.data)
            current = current.next
        return str(result)  # 결과 리스트를 문자열로 변환하여 반환

# sll = SinglyLinkedList()
# sll.append(1)
# sll.append(2)
# sll.append(3)
# print(sll)  # [1, 2, 3]

# deleted_item = sll.delete(1)
# print(f"Deleted item: {deleted_item}")  # 2
# print(sll)  # [1, 2, 3]