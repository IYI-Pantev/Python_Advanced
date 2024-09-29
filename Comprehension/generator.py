from sys import getsizeof

genValues = (x * 3 for x in range(1, 100000))
print(type(genValues))

print("gen:", getsizeof(genValues), 'bytes')

# values = [x * 3 for x in range(1, 100000)]
# print(type(values))

# print("gen:", getsizeof(values), 'bytes')
