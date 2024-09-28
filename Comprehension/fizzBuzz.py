def fizzBuzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return 'fizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'

    return num


print(fizzBuzz(7))
print('- - - ')
print(fizzBuzz(3))
print('- - - ')
print(fizzBuzz(5))
print('- - - ')
print(fizzBuzz(15))
print('- end -')
