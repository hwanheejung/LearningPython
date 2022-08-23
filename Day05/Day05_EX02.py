"""
1. for문 이용해서, 0 1 2 3 4 5 6 7 출력

2. list ["Mon", "Tue", "Wed", "Thu", "Fri"]
len 이용해서 리스트 요소 개수
"""

# ----- Problem 1 ----- #
for i in range(8):
    print(i, end=' ')

# ----- Problem 2 ----- #
weekday = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print("\n리스트 요소 개수: {}".format(len(weekday)))
