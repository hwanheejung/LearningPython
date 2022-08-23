# Review 'Class'

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def play(self):
        print("{} 선수({}세), 경기에 출전합니다"
              .format(self.name, self.age))

sonny = Player("손흥민", 30)
sonny.play()


