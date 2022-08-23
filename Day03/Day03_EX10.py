"""
짝수 or 홀수
<idea>
짝수는 나머지가 0, 홀수는 나머지 1
"""
n = 1
while True:
    print("--------{}번째 play--------".format(n))
    num = int(input("숫자를 입력하세요: "))

    if num == 0:
        print("0입니다.")
    elif num % 2 == 0:
        print("{}는 짝수입니다.".format(num))
    elif num % 2 == 1:
        print("{}는 홀수입니다.".format(num))

    quit = input("quit? (yes/no) ")
    elif quit == "yes":
        print("{}번 플레이하셨습니다.".format(n))
        break
    n += 1