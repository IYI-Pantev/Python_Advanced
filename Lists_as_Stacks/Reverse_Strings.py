text = "I love Python"

s = []

for ch in text:
    s.append(ch)

result = ''

while s:
    result += s.pop()

print(result)

# s = [1, 6, 7, 9]
#
# print(*s)

# text = list(input("Please enter: "))
#
# print(text)