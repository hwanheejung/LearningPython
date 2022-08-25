# Cont.
"""
What is 'Heap'?
    - upgrade version of 'Tree'
    - Pseudo Code
      Add 1) tree와 동일하게 노드를 끝에 추가
          2) while 부모 노드 있는지 확인 -> 있으면, if 부모 노드 < 새 노드 : 비교해서 자리 바꿈
                                         else: break
                                      -> 없으면, break
      Delete 1) Root node와 끝 노드 change
             2) tree처럼 끝 노드 delete
             3) while 자식 노드가 있는지 확인 -> 있으면, if 부모 노드 < 큰 자식 노드: change
                                                    else: break
                                           -> 없으면, break

"""

"""
백준 11279 : 최대 힙
13
input: 0 1 2 0 0 3 2 1 0 0 0 0 0    
output: 0 2 1 3 2 1 0 0
9
input: 8 0 1 2 7 0 0 0 3
output: 8 7 2 1
"""

class Heap:
    def __init__(self):
        self.size = 13
        self.heap = [None] * self.size
        self.cursor = 1

    def isFull(self):
        if self.cursor == self.size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.cursor == 1:
            return True
        else:
            return False

    def parent(self, child):
        if child == 1:
            return False
        elif child // 2 >= 1:
            return self.heap[self.cursor // 2]
        else:
            return False

    def children(self, parent):
        if parent * 2 + 1 <= self.size:
            self.chd1 = self.heap[parent * 2]
            self.chd2 = self.heap[parent * 2 + 1]
            return self.chd1, self.chd2


    def add(self, item):
        if not self.isFull():
            self.heap[self.cursor] = item
            while self.parent():
                if
            """
            2) while 부모 노드 있는지 확인 -> 있으면, if 부모 노드 < 새 노드 : 비교해서 자리 바꿈
                                             else: break
                                          -> 없으면, break"""

    def delete(self):

h = Heap()
