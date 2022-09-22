"""
What is 'Tree'?
- 계층적 구조 (부모 / 자식 관계)
- 비선형
- 자식은 최대 2개

       1
     2   3          [  , 1, 2, 3, 4, 5, 6, 7]
    4 5 6 7
- N의 자식: 2N, 2N + 1
- X의 부모: X // 2

- add : 트리 끝에 노드 추가
- delete : 트리 끝의 노드 삭제
"""

class Tree:
    def __init__(self):
        self.cursor = 1
        self.size = 8
        self.t = [None] * self.size

    def show_parent(self, position):
        if position == 1:
            print("Root Node")
        # position이 트리 범위 안에 들어오는지
        elif position // 2 >= 1:
            print(self.t[position // 2])
        else:
            print("out of range")

    def show_left_child(self, position):
        if position * 2 <= self.size:
            print(self.t[position * 2])
        else:
            print("out of range")

    def show_right_child(self, position):
        if position * 2 + 1 <= self.size:
            print(self.t[position * 2 + 1])
        else:
            print("out of range")

    def add(self, item):
        if not self.isFull():      # self.isFull() == False / 다른 언어: if !self.isFull()
            self.t[self.cursor] = item
            self.cursor = self.cursor + 1

    def delete(self):
        if not self.isEmpty():
            self.t[self.cursor - 1] = [None]
            self.cursor = self.cursor - 1

    def isEmpty(self):
        if self.cursor == 1:
            return True
        else:
            return False

    def isFull(self):
        if self.cursor == self.size:
            return True
        else:
            return False

    def display(self):
        index = 1
        while index <= self.cursor - 1:
            print(self.t[index], end = " ")
            index += 1
        print()



tree = Tree()
tree.add('a')
tree.add('b')
tree.add('c')
tree.add('d')
tree.add('e')
tree.add('f')
tree.add('g')
tree.display()

tree.show_parent(3)         # 'a'
tree.show_right_child(2)    # 'e'
tree.show_left_child(2)     # 'd'

tree.delete()
tree.delete()

tree.display()
