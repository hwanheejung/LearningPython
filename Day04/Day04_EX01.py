"""
버스요금
"""

money = 10000
print("나이: ")
age = int(input())
count = 0

def bus():
    global money, count
    if age >= 19:
        print("성인입니다")
        money -= 1250
    else:
        print("학생입니다")
        money -= 900
    count += 1

bus()
bus()

print("저는 버스를 {}회 탔고, 잔액은 {}원입니다.".format(count, money))