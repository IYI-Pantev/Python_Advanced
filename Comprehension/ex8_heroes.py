# import sys
# from io import StringIO

data_input = """Peter, George
Peter-Sword-20
Peter-Shield-10
George-Gem-100
Peter-Sword-15
George-Sword-20
End"""
# sys.stdin = StringIO()

heroes = input().split(", ")
inventory = {hero: {} for hero in heroes}
while True:
    command = input()
    if command == "End":
        break
    hero, item, cost = command.split("-")
    if item not in inventory[hero]:
        inventory[hero][item] = int(cost)

for hero in heroes:
    cost = sum(inventory[hero].values())
    items = len(inventory[hero])
    print(f"{hero} -> Items: {items}, Cost: {cost}")
