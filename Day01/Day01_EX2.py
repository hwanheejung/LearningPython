# num1과 num2의 값을 바꿔라
num1 = 5
num2 = 7

""" 
Idea 
num3라는 변수를 추가하여 num2의 7을 num3에 옮기고, num1의 5를 num2에 옮기고, num3의 7을 num1에 옮긴다. 
"""

num3 = num2     # num3에 num2 대입 -> temp = 7
num2 = num1     # num2에 num1 대입 -> num2 = 5
num1 = num3     # num1에 num3 대입 -> num1 = 7

print(num1)     # 7
print(num2)     # 5

# 주석처리 단축키 : Ctrl + /
