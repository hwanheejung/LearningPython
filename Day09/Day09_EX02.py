"""
What is 'Tuple'?
    - 요소 값이 변경(생성, 삭제, 수정)이 되지 않는 (파이썬의) 리스트
    - [리스트] (튜플)
"""

L = [1, 2, 3, 4, 5]     # list
L2 = [6, 7, 8]
T = (1, 2, 3, 4, 5)     # tuple
T2 = (6, 7, 8)

# 전체 출력
print(L)
print(T)

# 요소 출력
print(L[2])
print(T[2])

# 부분 출력 (슬라이싱)
print(L[1:4])
print(T[1:4])

# 통째로 추가하는건 됨
L = L + L2
T = T + T2
print(L)
print(T)

# 원소 수정
L[2] = 10       # index 2에 원소 10 대입
del L[0]        # index 0 원소 삭제
print(L)

# T[2] = 10     # 'tuple' object does not support item assignment

# 원소가 1개인 튜플
L4 = [13]
T4 = (13, )