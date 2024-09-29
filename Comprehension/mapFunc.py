items = [
    ("Products1", 10),
    ("Products2", 8),
    ("Products3", 12),
]

prices = list(map(lambda item: item[1], items))

print(prices)

# prices = []
# for item in items:
#     prices.append(item[1])

# map iterable object
