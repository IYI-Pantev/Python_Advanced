def Fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx - 1) + Fibonacci(idx - 2)


print(Fibonacci(8))
