print(1)


# class BadmanError(Exception):
#     pass
#
#
# raise BadmanError('Error rrrr...')

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print("An error occurred:", str(e))