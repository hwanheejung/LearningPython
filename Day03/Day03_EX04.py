x = 10

def fn():
    y = 100
    global x
    x = 20
    x = x + y

fn()
print(x)
