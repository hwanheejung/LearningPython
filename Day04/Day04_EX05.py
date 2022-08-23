"""
for (요소) in (list):
    # 요소 개수만큼 자동으로 index +1 하면서 한바퀴씩 돌며 요소를 하나씩 꺼내 쓸거라는 뜻
"""
# Practice 01 : 순서대로 출력
foods = ["pasta", "pizza", "burger", "salad"]

for food in foods:
    print(food)

# Practice 02 : 순서대로 출력
num = [11, 22, 77, 99, 100]

for n in num:
    print(n)

# Practice 03
for i in range(5):
    print(2 * (i + 1))