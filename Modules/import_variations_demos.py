from random import randint as gimme_number

try:
    print(gimme_number(1, 101))
    print(randint(1, 100))
except NameError as t:
    print('when module is customly named we need to stick to it.\n', str(t))
finally:
    print('---end---')
