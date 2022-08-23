
class Car:  # 자동차 만드는 설명서
    def __init__(self, ms):     # 모든 클래스의 생성자는 __init__()
        self.maxSpeed = ms

    def info(self):
        print("my max speed is {}.".format(self.maxSpeed))


genesis = Car(200)
genesis.info()

tico = Car(150)
tico.info()

