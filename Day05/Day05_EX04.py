"""
------ 자료구조의 리스트 --------- 파이썬 리스트 ---------
- 일렬로 빈칸없이 나열되어 있음
- 순서를 가지고 있음           = list[0], list[1]...
- 원하는 위치에 데이터 추가     = list.insert(2,"a")
- 원하는 데이터 삭제           = list.remove("a")
- 원하는 위치의 데이터 삭제     = del list[0]
"""

MT_list = ["Kim", "Lee", "Jung", "Park"]
print("- MT_list: ", MT_list)

""" ----- list.append(), list.insert(), list.remove() ----- """
# 마지막자리에 추가
MT_list.append("Moon")
print("- list.append(): ", MT_list)

# 원하는 위치에 추가
MT_list.insert(1, "Choi")
print("- list.insert: : ", MT_list)

# 리스트 추가
MT_list.extend(["Jang", "Gang", "Heo"])
print("- list.extend: ", MT_list)

# 특정 요소 제거
MT_list.remove("Park")
print("- list.remove: ", MT_list)

# 특정 자리의 요소 제거
del MT_list[3]
print("- del list: ", MT_list)

""" ----- list.sort(), sorted(list) ----- """
# list 정렬. 저장X
sorted_MT_list = sorted(MT_list)
print("- sorted(list): ", sorted_MT_list)

# list를 정렬해서 교체 (기존 리스트 덮어쓰기)
MT_list.sort()
print("- list.sort: ", MT_list)

""" ----- list.count ----- """
# 특정 요소의 개수
print("- list.count: ", MT_list.count("Choi"))
