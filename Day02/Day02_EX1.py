"""
9~12 : fall
8~6 : summer
5~3 : spring
2~1 : winter
"""

def season(month):
    if month > 12:
        print("1~12의 값을 입력하세요.")
    elif month >= 9:
        print("fall")
    elif month >= 6:
        print("summer")
    elif month >= 3:
        print("spring")
    else:
        print("winter")

print("month:")
month = input()
season(int(month))

