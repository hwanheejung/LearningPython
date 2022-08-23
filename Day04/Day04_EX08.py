# Incomplete
"""
Algorithm 2
-----삽입정렬-----
<idea>
    key는 1부터 마지막 idx까지의 요소.
    key 앞의 요소와 비교해서 key가 더 작으면 자리바꿈
    key_idx - (1..2..3..)
"""
num = [4, 3, 2, 10, 12, 1, 5, 6]
key_idx = 1

while key_idx < len(num):
    print(num)
    print("Key:{}".format(num[key_idx]))

    for i in range(key_idx):
        print(num[key_idx - i - 1])
        if num[key_idx] < num[key_idx - i - 1]:
            for j in range(key_idx):
                num[key_idx-i] = num[key_idx-j-1]


    key_idx += 1

