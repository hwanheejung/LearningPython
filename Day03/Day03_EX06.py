num = [10, 20, 30, 40, 50]

""" 
---하나씩 출력---
print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])
"""

index = 0
# sol 1
while index < 5:
    if num[index] == 20:
        print("20이 있습니다")
        break
    else:
        index += 1

# sol 2
if 20 in num:
    print("20이 있습니다")


#
# while index <= 4:
#     print(num[index])
#     index += 1

