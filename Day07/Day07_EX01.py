""" <Algorithm>
리스트 뒤에서부터 출력하는데, 중복된 수는 제외하고 출력
songa.kim@kakao.com
"""

arr = [2, 2, 3, 1, 3]
result = []
arr.reverse()

for value in arr:
    if value not in result:
        result.append(value)

print(result)


