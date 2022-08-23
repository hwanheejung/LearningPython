"""
숫자(정수) 하나를 입력 받고, 입력받은 숫자보다 작은 5의 배수 모두 출력
"""

num = int(input())
five = 5

while five <= num:
    print(five)
    five += 5
