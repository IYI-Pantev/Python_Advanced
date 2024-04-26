class ValueCannotBeNegativeError(Exception):
    """only positive numbers are allowed!"""
    pass


numbers = [1, 2, -3, 4, 5]

for number in numbers:
    if number < 0:
        raise ValueCannotBeNegativeError('only positive numbers are allowed!')
