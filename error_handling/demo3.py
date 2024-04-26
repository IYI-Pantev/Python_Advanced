def raise_exception():
    int('asd')
    pass


def f1():
    try:
        raise_exception()
        return 1
    except ValueError as err:
        return 2
    finally:
        print('finally always returns')


x = f1()
print(x)
