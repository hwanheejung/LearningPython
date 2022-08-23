# ---함수---

# def hello():
#     print("안녕하세요")
#     print("저는 정환희입니다")
#     print("감사합니다")
#
# hello()

print("num1 =")
num1 = input()
print("num2 = ")
num2 = input()

def plus(n1, n2):
    return n1 + n2

result = plus(int(num1), int(num2))   #result = num1 + num2

print("result =", result)
