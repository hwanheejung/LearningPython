dates_of_month = {
    "1월" : 31,
    "2월" : 28,
    "3월" : 31,
    "4월" : 30,
    "5월" : 31,
    "6월" : 30
}

# 월을 입력하세요 ex. 1 or 2 or 6

while True:
    mon = input("월을 입력하세요 > ")
    mon += "월"
    print("{}은 {}일까지 있습니다.".format(mon, dates_of_month[mon]))

