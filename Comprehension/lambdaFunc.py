
# lambda is simple
# one line anonymous function

items = [
    ("Products1", 10),
    ("Products2", 8),
    ("Products3", 12),

]


# def sort_item(item):
#     return item[1]


items.sort(key=lambda item: item[1], reverse=True)
print(items)
