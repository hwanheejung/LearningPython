"""
What is 'Class'?
    생성자:
        - 클래스 이름과 이름이 같은 특별한 함수
        - 기능: 클래스를 보고 객체 생성
        - 객체 생성 빼고 딱히 할일이 없으면, 개발자가 굳이 구현을 직접 안함(생략되어 있는 것)
    -> Day07_EX05

    self:
        - 객체 그 자신
        - 클래스 외부에서 클래스 함수를 부를 때 누가 불렀는지 확인하는 용도
"""

# class 생성
class Snack:
    def ASMR(self):
        print("바삭바삭")

potatochip = Snack()
potatochip.ASMR()

sumichip = Snack()
sumichip.ASMR()

