# square = lambda x: x ** 2
# print(square(5))  # Output: 25
#
# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mydoubler(11))
# print(mytripler(11))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
