"""
Linear Queue
- isFull : 줄을 더이상 못쓰게 할 때
- isEmpty : 줄이 없을 때

Circular Queue
- isEmpty : front, rear가 같은 곳을 가리킬 때    front == rear
    enqueue: rear가 가리키는 곳에 추가
    dequeue: front가 가리키는 곳을 삭제
- isFull : front보다 rear가 한 칸 전에 있을 때
    front - 1 = rear
"""

# Circular Queue
class Queue:
    def __init__(self):
        # 초기화 : front, rear를 index 0 으로 설정
        self.front = 0
        self.rear = 0
        self.size = 5       # queue의 크기
        self.queueList = [None] * self.size     # 텅 빈 5칸 리스트

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        # rear가 front보다 한 칸 앞에 있으면
        # front가 rear보다 한 칸 뒤에 있으면
        if self.front == (self.rear + 1) % self.size:
            return True
        else:
            return False

    def enqueue(self, item):
        # isFull == False일 때
        # item을 rear 자리에 넣어주는 역할
        # rear가 한 칸 전진
        self.queueList[self.rear] = item
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        # isEmpty == False일 때
        # front 자리의 값을 제거
        # front 한 칸 전진
        self.queueList[self.front] = [None]     # python에서만 성립. 다른 언어에서는 변수 안에 값을 제거하는것 자체가 없기 때문에,
                                                # 자료구조를 표현(= 값이 제거됐다 etc..) 자료구조의 범위(front~ rear-1)
        self.front = (self.front + 1) % self.size

    def display(self):  # front ~ rear-1 까지만 출력
        index = self.front
        while index <= self.rear - 1:
            print(self.queueList[index], end = " ")
            index += 1
        print()


q = Queue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.enqueue(1)
q.display()

q.dequeue()
q.dequeue()
q.dequeue()
q.display()

print(q.isFull())
q.dequeue()
print(q.isEmpty())
