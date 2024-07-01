n = int(input())

s = []

for _ in range(n):
    query = input()
    if query.startswith('1'):
        data = query.split(' ')
        element = int(data[1])
        s.append(element)
    elif query == '2':
        if len(s) > 0:
            s.pop()
    elif query == '3':
        if len(s) > 0:
            print(max(s))
    elif query == '4':
        if len(s) > 0:
            print(min(s))

str_s = [str(i) for i in s]
reversed_s = []
while str_s:
    reversed_s.append(str_s.pop())
print(', '.join(reversed_s))
