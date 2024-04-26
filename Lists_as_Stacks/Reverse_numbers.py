numbers = input().split(' ')


result = ''

while numbers:
    result += numbers.pop() + ' '

print(result)