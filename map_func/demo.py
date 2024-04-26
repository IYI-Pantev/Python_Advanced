# Map Function - map(function, iterable)
#              - Returns an iterator that applies to every item of iterable

def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num


x = [551, 641, 122, 453, 234, 343]

y = list(map(make_even, x))
print(y)
