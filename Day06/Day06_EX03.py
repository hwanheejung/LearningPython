"""
행동을 선택하세요
1 --> 1) 빵이 없으면 알바생을 불러 빵 추가 후 구매
      2) 고객은 00를 구매했습니다. (단, 고객은 제일 앞에 보이는 빵을 구매한다.)
2 --> 1) 진열대 확인
      2) 진열대에 빵이 3개 이하면, 빵 추가 (빵은 알바생이 storage에서 랜덤으로 추가)
         진열대에는 []가 있습니다.
3 --> 영업 종료. 매출액 계산

손님의 진열대 시점: 뒤[]앞
빵: 2000원
"""

def check():
    print("진열대: {}".format(bread))

def addBread():
    storage = ["메론맛", "딸기맛", "초코맛", "우유맛"]
    import random
    add_random = random.choice(storage)
    bread.append(add_random)
    print("알바생: 진열대에 빵이 3개 이하라서, {}을 1개 추가했습니다.".format(add_random))

def buy():
    buy = bread.pop()
    print("손님이 {}을(를) 구매했습니다.".format(buy))

bread = ["초코맛", "딸기맛"]
cus = 1
earn = 0

while True:

    num = int(input(">>> 행동을 선택하세요: 1. 빵 구매 2. 진열대 확인 3. 종료 >> "))

    if num == 1:
        print("----- {}번째 손님 -----".format(cus))
        if len(bread) == 0:
            print("상품이 없습니다. 알바생을 부르세요")

            addBread()
            check()
            buy()

        else:
            buy()
            check()
        cus += 1
        earn += 2000

    elif num == 2:
        if len(bread) >= 3:
            check()
        else:
            addBread()
            check()

    elif num == 3:
        print("영업 종료. 오늘의 매출액: {}원".format(earn))
        break



