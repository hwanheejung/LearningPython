# Review

class Cat:
    count = 0

    def appear(self):
        print("고양이가 한마리 나타났습니다. 야옹!")
        Cat.count += 1
        print("지금까지 고양이는 총 {}마리 나왔습니다.".format(Cat.count))


nabi = Cat()
nabi.appear()

yaong = Cat()
yaong.appear()


"""
cf.
__name__ : public
    프로젝트 안에서 마음대로 불러쓸 수 있는 오픈마인드 변수, 함수
__name : private
    클래스 밖을 나가면 아무도 못 부르는 변수, 함수
"""

