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
        self.size = 8
        self.t = [None] * self.size

    def show_parent(self, position):
        if position // 2 >= 1:
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

t = Tree()
t.show_parent(3)
t.show_right_child(3)




