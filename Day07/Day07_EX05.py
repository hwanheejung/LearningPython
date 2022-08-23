"""
# Review 'Class'

self: 클래스 외부에서 클래스 함수를 부를 때 누가 불렀는지 확인하는 용도
"""
class Barista:
    # 생성자
    def __init__(self, name):     # 개발자가 직접 생성자를 구현
        self.name = name
        
    def hello(self):
        print("Welcome! I'm barista {}.".format(self.name))
    def serve(self):
        print("your coffee's here")

barista = Barista("Mike")     # 생성자 호출 --> 객체 내 변수를 갖고 태어남
barista.hello()
barista.serve()

