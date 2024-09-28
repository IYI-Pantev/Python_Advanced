# def f1(index, n):
#     if index == n:
#         return  # base case / exit condition
#     print(index)
#     f1(index + 1, n=n)  # recursive case
#
# #
# f1(index=0, n=10)

# Fibonacci
# f(n) = f(n-1)+f(n-2)
# f(1) = f(0) = 0
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
