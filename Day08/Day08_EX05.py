
class Snack:
    companyName = "해태"
    def __init__(self, snackName, snackPrice):
        self.snackName = snackName
        self.snackPrice = snackPrice

    def info(self):
        print("{}(제조 회사: {}, 가격: {}원)"
              .format(self.snackName, Snack.companyName, self.snackPrice))

pepero = Snack("pepero", 1500)
potatochip = Snack("potatochip", 1800)

pepero.info()
potatochip.info()

# 오리온에서 회사 인수함
Snack.companyName = "오리온"
pepero.info()
potatochip.info()
