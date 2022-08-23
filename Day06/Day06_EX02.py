"""
----- What is 'Stack'? -----
- 일렬로 나열되어 있음
- 순서를 가지고 있음
- 추가: 제일 위에(뒤에)     = list.append()
- 삭제: 제일 위에(뒤에)     = list.pop()
-> like stacking rocks
-> 제한된 list

list :: array + insert(), del, remove()
stack :: array + pop(), append()
"""

elevator = ["Kim", "Son", "Lee", "Jung", "Go"]

elevator.pop()      # ["Kim", "Son", "Lee", "Jung"]
elevator.pop()      # ["Kim", "Son", "Lee"]
elevator.pop()      # ["Kim", "Son"]
print(elevator)

elevator.append("Lim")      # ["Kim", "Son", "Lim"]
print(elevator)
elevator.pop()              # ["Kim", "Son"]
print(elevator)

""" ----- 마지막 요소 찾기 ----- """
# Sol 1 : pop()함수를 사용하여 목록의 마지막 요소 가져 오기
"""
def pop():
    제일 마지막 원소를 제거하고, 
    return list의 제일 마지막 원소
"""
last = elevator.pop()
print(last)

# Sol 2 : index -1로 목록의 마지막 요소 가져 오기
print(elevator[-1])

