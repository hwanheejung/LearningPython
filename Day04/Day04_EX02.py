"""
how many 7 in num?
"""

num = [7, 8, 1, 5, 2, 7, 7]
index = 0
count = 0

while index < len(num):
    if num[index] == 7:
        count += 1

    index += 1

print("7이 {}개 있습니다.".format(count))

