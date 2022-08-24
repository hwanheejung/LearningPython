"""
가위바위보 게임
"""
win = {
    "가위" : "바위",
    "바위" : "보",
    "보" : "가위"
}

def game(computer, me):
    result = 0
    if computer == me:
        result = "Draw"
        return result
    elif win[me] == computer:
        result = "Win"
        return result
    elif win[computer] == me:
        result = "Lose"
        return result

while True:
    me = input(">> me: ")       # 나

    if me == "stop":
        print("Game Over")
        break

    else:
        import random
        RSP = ["가위", "바위", "보"]
        computer = random.choice(RSP)
        print("Result: {} \n me: {} \n computer: {}".format(game(computer, me), computer, me))





