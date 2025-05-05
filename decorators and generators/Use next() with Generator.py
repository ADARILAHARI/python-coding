def counter():
    yield 1
    yield 2
    yield 3

g = counter()
print(next(g))  # 1
print(next(g))  # 2
