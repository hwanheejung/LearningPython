"""
Linear Queue
- isFull : 줄을 더이상 못쓰게 할 때
- isEmpty : 줄이 없을 때

Circular Queue
- isEmpty : front, rear가 같은 곳을 가리킬 때
    enqueue: rear가 가리키는 곳에 추가
    dequeue: front가 가리키는 곳을 삭제
- isFull : front보다 rear가 한 칸 전에 있을 때
    front -1 = rear
"""



class Queue: # 초기화 : front, rear를 index 0 으로 설정
    def __init__(self, front, rear):
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):

    def enqueue(self):

    def dequeue(self):



