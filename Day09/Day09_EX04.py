""" <Algorithm>
input: [2, 2, 3, 1, 3]  output: [2, 1, 1, 1]
input: [7, 8, 8, 9]  output: [1, 2, 1]
input: [3, 3, 4, 5, 6, 3, 7]  output: [2, 1, 1, 1, 1, 1]
input: [2, 6, 6, 6, 3]  output: [1, 3, 1]
"""


input = [4, 2, 2, 2]
output = []

index = 0
num = 1
while index < len(input) - 1:
    if input[index] != input[index + 1]:
        output.append(1)
        index += 1

    else:
        n = 1
        while n < len(input) - index - 1:
            if input[index] == input[index + n]:
                num += 1
            else:
                break
            n += 1
        output.append(num)
        index += num

if input[-1] != input[-2]:
    output.append(1)
else:
    output[-1] += 1

print(output)

