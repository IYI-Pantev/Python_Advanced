# def square_numbers(nums):
#     for i in nums:
#         yield (i * i)


# gen_numns = square_numbers([1, 2, 3, 4, 5])

# print(gen_numns)
# print('- - -')

# print(next(gen_numns))
# print(next(gen_numns))
# print(next(gen_numns))

genNums = (x*x for x in range(1, 6))
print(genNums)
