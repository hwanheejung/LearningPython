"""참석명단"""

MT_list = ["Kim", "Lee", "Jung", "Park"]

# ----- Sol 1 : while
idx = 0
while idx < len(MT_list):
    print(MT_list[idx], end=" ")
    idx += 1

# ----- Sol 2 : for
print()
for p in range(len(MT_list)):
    print(MT_list[p], end=" ")


