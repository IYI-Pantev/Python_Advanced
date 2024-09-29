# values = list(range(5))

# values1 = [*range(5)]

# letters = [*values, 'hi', *values1]
# print(letters)

first = {"x": 1}
second = {"x": 20, "y": 3}

combined = {**first, **second, "a": 33}

print(combined)
