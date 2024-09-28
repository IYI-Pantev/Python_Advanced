def sqauare(x):
    return x * x

f_2 = sqauare
print(sqauare)
print(f_2)

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

func = my_map(lambda x: x * x, [2, 3 ,7])
print(func)

str1 = 'GeeksforGeeks'
 
# upper = lambda string: string.upper()
# print(upper(str1))

def to_upper(string):
    return string.upper()

print(to_upper(str1))
numbers = [3, 23, 14, 2]
result = map(f_2, numbers)
print(result)
print(list(result))