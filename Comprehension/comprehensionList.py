items = [
    ("Products1", 10),
    ("Products2", 8),
    ("Products3", 12),

]

prices = [item[1] for item in items]
prices.sort(reverse=True)
print(prices)

higher_prices = [item for item in items if item[1] >= 10]
print(higher_prices)
