# 나이 매개변수로 1개, 19세 이상이면 성인 / 19세 미만이면 청소년입니다

def person(age):
    if age >= 19:
        print("성인입니다")
    else:
        print("청소년입니다")

person(23)
person(17)

print("age :")
age = input()

person(int(age))




