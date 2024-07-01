from collections import deque

food = 348

orders = '20 54 30 16 7 9'
ord_list = orders.split(' ')
ord_nums = [int(i) for i in ord_list]

q = deque(ord_nums)
print(max(q))

while True:

    if len(q) > 0:
        current_order = q.popleft()
        if food - current_order > 0:
            food -= current_order
        else:
            print(f'Orders left: {current_order}{" ".join([str(i) for i in list(q)])}')
            break
    else:
        print('Orders complete')
        break
