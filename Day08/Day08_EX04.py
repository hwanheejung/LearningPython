
class Beer:
    companyName = "Lotte"

    def __init__(self, beerName):
        self.beerName = beerName

    def advertise(self):
        print("{}에서 만든 {}맥주입니다".format(Beer.companyName, self.beerName))


kloud = Beer("kloud")
fitz = Beer("fitz")

kloud.advertise()
fitz.advertise()

# 회사 인수
Beer.companyName = "OB"     # 클래스 변수는 클래스 밖에서 쓸 수 있음.
kloud.advertise()
fitz.advertise()