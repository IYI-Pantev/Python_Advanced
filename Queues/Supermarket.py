from collections import deque

q = deque()

text = input()

while text != 'End':

    if text == 'Paid':
        while q:
            print(q.popleft())
    if text != 'Paid':
        q.append(text)
    text = input()

print(f"{len(q)} people remaining.")

