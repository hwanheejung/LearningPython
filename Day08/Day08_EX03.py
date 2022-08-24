class Family:
    address = ""        # 클래스 변수
    def __init__(self, name, address):
        self.name = name
        Family.address = address

    def info(self):
        print("저는 {}이구요, {}에 살고 있어요."
              .format(self.name, Family.address))

    def move(self, address):
        Family.address = address


dad = Family("아빠", "서울")
dad.info()

son = Family("아들", "서울")
son.info()

dad.move("부산")
son.info()
dad.info()