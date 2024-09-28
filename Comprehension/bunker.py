data_input = """food, water, materials, metal
5
food - pizza - quantity:10;quality:5
water - mineral - quantity:5;quality:10
materials - wood - quantity:2;quality:5
metal - copper - quantity:3;quality:10
food - burgers - quantity:5;quality:2
"""

categories = input(", ")
n = int(input())

for _ in range(n):
    category, item_name, quantity_quality = input().split(" - ")
    quantity, quality = quantity_quality.split(";")
    quantity, quality = quantity.split(":")[1], quality.split(":")[1]
    quantity, quality = int(quantity), int(quality)

    print(category, item_name, quantity, quality)
