# Review 'Class'

class Member:
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def enter(self):
        self.count += 1
        print("{}님 입장 | 입장 횟수: {}회".format(self.name, self.count))


jhh = Member("정환희", 0)
jhh.enter()
jhh.enter()
jhh.enter()


