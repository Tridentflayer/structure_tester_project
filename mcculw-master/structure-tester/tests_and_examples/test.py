import itertools as itrt
t = []

def func():
    for cnt in itrt.count():
        t = cnt /10
        y = 0
        y += 1
        yield t, y

func = func()

def run(data):
    t, y = next(data)
    for i in range(10):
        print(t)
        print(y)

run(func)