""" <Algorithm>
리스트 뒤에서부터 출력하는데, 중복된 수는 제외하고 출력
ex)
    input: [2, 2, 3, 1, 3]          output: [3, 1, 2]
    input: [7, 1, 2, 3, 3, 2, 1]    output: [1, 2, 3, 7]
"""

# Sol 1 : Clean Code
arr = [2, 2, 3, 1, 3]
result = []
arr.reverse()

for value in arr:
    if value not in result:
        result.append(value)

print(result)


# Sol 2 : Using 'Tuple'
input_T = (7, 1, 2, 3, 3, 2, 1)
input = [7, 1, 2, 3, 3, 2, 1]
output = []

index = 0
while index < len(input_T):         # len(input)을 쓰면, while이 돌면서 리스트의 길이가 줄어드는 문제 발생 -> tuple 사용
    result = input.pop()            # pop() 1) 리스트 끝 요소 제거 2) 제거된 요소 알려줌
    if result in output:
        pass
    else:
        output.append(result)
    index += 1

print(output)


