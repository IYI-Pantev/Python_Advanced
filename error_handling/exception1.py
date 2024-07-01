
try:
    # f = open('error_handling/test_file.txt')
    # var = bad_bar
    print(1 + 2)
except FileNotFoundError:
    print('ERROR No Such File')
except NameError as n:
    print(n)
# else:
    # print(f.read())
    # f.close()
finally:
    print("Executing finally")