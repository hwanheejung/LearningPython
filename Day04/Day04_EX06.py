"""
Algorithm 1
-----버블정렬-----
"""

num = [9, 1, 7, 2, 3, 8, 10, 0, 4]

idx = 0
while idx <= len(num) - 2:
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            blank = num[i]
            num[i] = num[i+1]
            num[i+1] = blank
    print("stage {}:".format(idx + 1), num)
    idx += 1

print("final result: ", num)


