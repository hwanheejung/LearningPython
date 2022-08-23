# num = [2, 4, 6, 1, 3]
#
# if num[0] > num[1]:
#     blank = num[0]
#     num[0] = num[1]
#     num[1] = blank
#
# print(num)


"""index 하나씩 작아져 1에서 멈추는 코드"""
num = [4, 3, 2, 10, 12, 1, 5, 6]

for n in range(len(num)-1, 0, -1):
    print(n)
