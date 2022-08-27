""" <Algorithm>
input: [2, 2, 3, 1, 3]          output: [2, 1, 1, 1]
input: [7, 8, 8, 9]             output: [1, 2, 1]
input: [3, 3, 4, 5, 6, 3, 7]    output: [2, 1, 1, 1, 1, 1]
input: [2, 6, 6, 6, 3]          output: [1, 3, 1]
input: [4, 2, 2, 2]             output: [1, 3]
"""

arr = [4, 2, 2, 2, 2]
result = []

idx = 0

while idx < len(arr) - 1:
    num = 1     # 비교해야할 개수
    n = 1       # 같은거
    while num <= len(arr) - idx - 1:
        if arr[idx] == arr[idx + num]:
            n += 1
        else:
            break
        num += 1
    result.append(n)
    idx += n

if arr[-2] != arr[-1]:
    result.append(1)

print(result)
