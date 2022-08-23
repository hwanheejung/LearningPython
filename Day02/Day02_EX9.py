
def buySnack(m):
    return m - 1000

print("주머니에 있는 돈이 얼마인가요?")
money = input()
money = int(money)
money = buySnack(money)

print(money)
