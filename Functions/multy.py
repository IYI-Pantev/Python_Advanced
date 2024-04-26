def multiply(*args):
    if not args:
        return None
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(1, 2, 3))
print(multiply())
