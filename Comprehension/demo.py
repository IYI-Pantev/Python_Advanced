# import types
#
#
# a_list = [1, 'f', 'g', 4, 8, True]
#
# only_nums = [e ** 2 for e in a_list if type(e) == types.]

# nums = [1, 2, 3, 4, 5, 6, 7]

# when if else - on the left/ only if right in comprehension
# filtered = ['Even' if x % 2 == 0 else 'Odd' for x in nums]
# print(filtered)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = sorted(car.items())

print(x)
dictionary = {key: value for (key, value) in car.items()}
print(dictionary)
dictionary["year"] = 2023
print(dictionary)
print('---new---')
nums = [4, 33]
cubes = {num: num ** 3 for num in nums}
print(cubes)
