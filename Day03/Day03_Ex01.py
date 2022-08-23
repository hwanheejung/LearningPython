# Review for Day02

"""
놀이공원
변수 count = 0
함수
1) enter (매개변수 X, return X) : count 1증가
2) out (매개변수 X, return X) : 출력
"""

count = 0

def enter():
    global count
    count += 1
    print("지금까지 입장한 고객은 총 {}명입니다.".format(count))

def out():
    print("안녕히 가세요.")

enter()
enter()
enter()
enter()
enter()
out()