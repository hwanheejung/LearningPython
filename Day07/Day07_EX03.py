"""
What is 'Queue'?
- upgrade version of stack
    stack: 누가 먼저 내릴래?
    queue: 누가 먼저 탈래? (탄 후의 순서는 상관 X / ex. 지하철 타는 순서)
- 자료구조의 일종: 리스트, 스택, 딕셔너리

- 순서를 가지고 있음
- 삽입(enqueue) : 뒤 (줄 서는 순서)
- 제거(dequeue) : 앞 (지하철 타는 순서)

"""

arr = [1, 2, 3, 4, 5]

# enqueue
arr.append(6)
print(arr)      # [1, 2, 3, 4, 5, 6]

# dequeue
del arr[0]
print(arr)      # [2, 3, 4, 5, 6]




"""
백준 2164
"""


