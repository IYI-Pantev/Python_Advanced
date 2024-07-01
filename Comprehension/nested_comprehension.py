# inner j is column/  outer i is row
print([[j for j in range(3)] for i in range(4)])

matrix = [[0, 1, 2], [1, 2, 3]]

flattened = [num for sublist in matrix for num in sublist]
# this is comprehensive version of the code below:
# f_nums = []
# for sublist in matrix:
#     for num in sublist:
#         f_nums.append(num)
print(flattened)
