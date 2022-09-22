"""
What is 'Dictionary'?

"""

number = {
  #  key  : value
    "one" : 1,
    "two" : 2,
    "three" : 3
}

print(number)
print(number["one"])

number["three"] = 33
print(number)

for key in number.keys():       # ["one", "two", "three"]
    print(key)

for value in number.values():   # [1, 2, 33]
    print(value)

for key, value in number.items():   #[("one", 1), ("two", 2), ("three", 33)]
    print("key:", key, "|| value:", value)

