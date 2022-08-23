"""
과일바구니 만들기
"""

def basket_print():
    print("바구니에", end=" ")
    for i in range(len(basket) - 1):  # 마지막 과일에도 ','가 붙기 때문에
        print(basket[i], end=", ")
    print(basket[-1], end="")  # 마지막 과일만 따로 출력
    print("이(가) 있습니다")


basket = ["딸기", "사과", "귤"]

while True:
    print()
    print("<< DIY 과일바구니 만들기 >>", end = " ")
    print("조회 / 추가 / 종료")
    menu = input("menu: ")

    if menu == "조회":
        basket_print()

    elif menu == "추가":
        add = input("넣고싶은 과일을 입력하세요: ")
        basket.append(add)

        basket_print()

    elif menu == "종료":
        print("종료되었습니다.")
        break









