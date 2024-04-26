from collections import deque

queue = deque()
n = int(input())

for _ in range(n):
    gas_pump = input().split(" ")
    queue.append([int(gas_pump[0]), int(gas_pump[1])])
print(queue)
dummy_queue = queue.copy()

for _ in range(n):
    # task is can we make a circle
    fuel_tank = 0
    flag = 0
    for pump in dummy_queue:
        fuel, distance_to_next = pump[0], pump[1]
        fuel_tank += fuel
        if fuel_tank < distance_to_next:
            break
        else:
            flag += 1
            fuel_tank -= distance_to_next
            if flag == len(queue):
                break
    if flag == len(queue):
        break

    dummy_queue.rotate(-1)


starting_index = dummy_queue.popleft()
print(queue.index(starting_index))

# data_inp = 3
# 1 5
# 10 3
# 3 4
