class Queue:
    # 생성자 함수
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1     # 출구
        self.rear = -1      # 입구

    # 꽉 찼니?
    def is_full(self):
        return self.rear == self.capacity -1
    # 비었니?
    def is_empty(self):
        return self.front == self.rear

    # 값 삽입
    def enqueue(self, item):
        if self.is_full():
            print('queue is full!!')
            return
        # 가득 안찼다면
        self.rear += 1
        self.items[self.rear] = item

    # 값 제거
    def dequeue(self):
        if self.is_empty():
            print('queue is empty!!')
            return
        # 값이 비어있지 않다면
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None
        return item


    
# queue = Queue()

# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)

# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.items)
# print(queue.peek())

# queue.enqueue(4)
# queue.enqueue(5)

# print(queue.items)
# print(queue.is_full())
# queue.enqueue(11)