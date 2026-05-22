

def add(*args):
    added = 0
    for n in args:
        added += n
    return added

print(add(6,7))

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=5)