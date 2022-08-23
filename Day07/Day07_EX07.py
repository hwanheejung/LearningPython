
class Computer:
    def __init__(self, company):
        self.company = company

    def powerOn(self):
        print("{} computer is on".format(self.company))

    def powerOff(self):
        print("{} computer is off".format(self.company))

samsung = Computer("samsung")
samsung.powerOn()
samsung.powerOff()

LG = Computer("LG")
LG.powerOn()
LG.powerOff()