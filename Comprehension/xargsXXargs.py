
# *args
def multiply(*nums):
    print(type(nums))
    total = 1
    for num in nums:
        total *= num
    return total


print(multiply(1, 2, 3, 4, 5))

# **kwargs


def save_user(**user):
    print(type(user))

    return f"User name: {user['name']}\nYears: {user['years']}"


print(save_user(name='Nick', years=29))
