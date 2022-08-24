"""
Algorithm 2
-----삽입정렬-----
"""

num = [4, 3, 2, 10, 12, 1, 5, 6]
key = 1

while key < len(num):        # key = 1, 2, 3, 4, 5, 6, 7
    for n in range(key, 0, -1):     # 비교할 요소의 개수(n)은 key 개수와 동일하기 때문에, key부터 0까지 -1씩 줄어들며 반복
        if num[n - 1] > num[n]:     # 앞의 요소가 뒤의 요소보다 크면, 둘이 자리바꿈
            blank = num[n - 1]
            num[n - 1] = num[n]
            num[n] = blank

        else:
            break
    key += 1
print(num)
