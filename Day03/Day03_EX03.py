# numnum = 7
#
# def sumNum(x,y,z):
#     print(numnum)
#     return x + y + z
#
#
# res = sumNum(2,3,4)
#
# print(res)

#
numnum = 7
def numPrint():
    global numnum
    numnum = 10


numPrint()
print("numnum의 값은 {}입니다".format(numnum))