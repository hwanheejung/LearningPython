# Review 'Class'

class Member:
    totalCount = 0

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def enter(self):
        self.count += 1
        Member.totalCount += 1
        print("{}님 입장 | 입장 횟수: {}회".format(self.name, self.count))
        print("총 입장 횟수: {}".format(Member.totalCount))
        print()


jhh = Member("정환희", 0)
jhh.enter()
jhh.enter()
jhh.enter()

tom = Member("Tom", 0)
tom.enter()
tom.enter()

