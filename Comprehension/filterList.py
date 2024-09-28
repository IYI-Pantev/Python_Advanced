items = [
    ("Products1", 10),
    ("Products2", 8),
    ("Products3", 12),
]

# filter iterable object
higher_prices = list(filter(lambda item: item[1] >= 10, items))

print(higher_prices)
