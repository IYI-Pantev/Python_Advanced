clothing = [int(i) for i in input().split(' ')]

box = []

rack_capacity = int(input())

number_of_racks = 1
current_rack_weight = 0

while clothing:
    cloth = clothing.pop()
    if cloth + current_rack_weight > rack_capacity:
        number_of_racks += 1
        current_rack_weight = 0

    current_rack_weight += cloth


print(number_of_racks)