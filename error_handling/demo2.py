def raise_exception():
    # raise TypeError/IndexError demonstration
    x = {}['asd']
    # x = [1][1]

    pass


try:
    raise_exception()
    print('no exception')
except IndexError:
    print('Index error handled')
except KeyError:
    print('Key error handled')

print('End')
