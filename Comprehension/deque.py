from collections import deque

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(len(queue))
print(queue[1])
