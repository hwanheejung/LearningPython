
class Car:
    def ride(self):
        print("달립니다!")

    def stop(self):
        print("멈춥니다!")

class Bus(Car):

    def ride(self):
        super().ride()      # super() : 부모 클래스 부르는 말
        print("씽씽!")
    def fee(self):
        print("요금을 받았습니다.")


bus = Bus()
bus.ride()
bus.fee()

