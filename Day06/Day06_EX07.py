win = {
    "가위" : "바위",
    "바위" : "보",
    "보" : "가위"
}

you = input("상대: ")
print("{} 내야 이김".format(win[you]))
