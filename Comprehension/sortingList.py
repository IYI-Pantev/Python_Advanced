# numbers = [3, 51, 2, 8, 8, 6]

# # .sort
# # numbers.sort(reverse=True)
# # print(numbers)

# print(sorted(numbers, reverse=True))

items = [
    ("Products1", 10),
    ("Products2", 8),
    ("Products3", 12),

]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
