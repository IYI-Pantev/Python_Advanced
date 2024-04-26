def f1(x, y, z):
    print(x, y, z)


def f2(x, *args):
    print(x)
    f1(*args)


print(f2(1, 2, 3, 4))
