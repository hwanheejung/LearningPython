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

- N의 자식: 2N, 2N + 1
- X의 부모: X // 2

"""
class Heap():
    def __init__(self):
        self.cursor = 1
        self.size = 13
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
                    self.heap[c//2], self.heap[c] = self.heap[c], self.heap[c//2]   # change
                else:
                    continue

    def delete(self):
        if not self.isEmpty():
            # root node와 끝노드 change
            if self.cursor == 2:
                del self.heap[1]
            else:
                self.heap[1], self.heap[self.cursor - 1] = self.heap[self.cursor - 1], self.heap[1]
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





heap = Heap()
heap.add(5) 
heap.add(1)
heap.add(7)
heap.add(8)
heap.add(2)
heap.add(10)
heap.add(11)
heap.delete()
heap.delete()


print(heap.heap)

