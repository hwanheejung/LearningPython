"""
백준 11279 : 최대 힙

input: 13 0 1 2 0 0 3 2 1 0 0 0 0 0
output: 0 2 1 3 2 1 0 0

input: 9 8 0 1 2 7 0 0 0 3
output: 8 7 2 1

0: del 가장 큰 숫자 출력하고 제거
int: add
"""

class Heap():
    def __init__(self):
        self.cursor = 1
        self.size = int(input())
        self.heap = [None] * self.size


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

    def add(self, item):
        if not self.isFull():
            self.heap[self.cursor] = item
            self.cursor += 1

            for c in range(self.cursor - 1, 1, -1):
                if c // 2 >= 1 and self.heap[c//2] < self.heap[c]:      # if 부모가 있고 and 부모<자식:
                    self.heap[c//2], self.heap[c] = self.heap[c], self.heap[c//2]   # swap
                else:
                    continue

    def delete(self):
        if self.isEmpty():
            print(0)

        if not self.isEmpty():
            # root node와 끝노드 swap
            if self.cursor == 2:
                print(self.heap[1])
                del self.heap[1]
            else:
                self.heap[1], self.heap[self.cursor - 1] = self.heap[self.cursor - 1], self.heap[1]
                print(self.heap[self.cursor - 1])
                del self.heap[self.cursor - 1]
            self.cursor -= 1

            # 정렬
            for c in range(1, self.cursor - 1, 1):
                # 자식이 둘: 1) 부모 < 자식1 or 자식 2 -> 큰자식과 바꿈  2) 부모 > 자식 둘 : cont.
                if self.heap[c * 2] is not None and self.heap[(c * 2) + 1] is not None:
                    if self.heap[c] < self.heap[c * 2] or self.heap[c] < self.heap[c * 2 + 1]:
                        if self.heap[c * 2] > self.heap[(c * 2) + 1]:
                            self.heap[c], self.heap[c * 2] = self.heap[c * 2], self.heap[c]
                        else:
                            self.heap[c], self.heap[(c * 2) + 1] = self.heap[(c * 2) + 1], self.heap[c]
                    else:
                        continue
                # 자식이 하나
                elif self.heap[c * 2] is not None and self.heap[(c * 2) + 1] is None:
                    if self.heap[c * 2] > self.heap[c]:
                        self.heap[c], self.heap[c * 2] = self.heap[c * 2], self.heap[c]
                    else:
                        continue
                # 자식이 없어
                else:
                    continue

    def display(self):
        index = 1
        while index <= self.cursor - 1:
            print(self.heap[index], end=" ")
            index += 1
        print()


heap = Heap()

for i in range(heap.size):
    x = int(input())
    if x == 0:
        heap.delete()
    elif x != 0:
        heap.add(x)








