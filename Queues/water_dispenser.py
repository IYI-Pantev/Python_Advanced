from collections import deque

START_COMMAND = 'Start'
END_COMMAND = 'End'
REFILL_COMMAND = 'Refill'

quantity = int(input())
people_queue = deque()

while True:
    name = input()
    if name == START_COMMAND:
        break
    people_queue.append(name)

while True:
    name = input()
    if name == END_COMMAND:
        print(f"{quantity} liters left")
        break
    if name.startswith(START_COMMAND):
        name_params = name.split(" ")
        refill_liters = int(name_params[1])
        quantity += refill_liters

    else:
        person = people_queue.popleft()
        person_liters = int(name)
        if quantity - person_liters > 0:
            print(f"{person} got water")
            quantity -= person_liters
        else:
            print(f"{person} must wait")
