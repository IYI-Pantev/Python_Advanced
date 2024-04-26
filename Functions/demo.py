def demo(*args, **kwargs):
    return f"the *data argument type is: {type(args)}, the ** is {type(kwargs)}\n" \
           f"{args}\n" \
           f"{kwargs}"


print(demo(33, 69, x=1, y=3))
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(*nums)

x = '(3, 3)'
print(eval(x))
print(type(eval(x))) # val is not good for user input

# def some_func(name, age):
#     print(f'{name} is {age} years old')
#
#
# # keys must match the parameters of the function
# person = {'age': 29, 'name': 'Peter'}
# some_func(**person)
