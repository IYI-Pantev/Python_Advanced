# simple way
# def evens(end_num):
#     for i in range(2, end_num + 1):
#         if i % 2 == 0:
#             print(i)
#
#
# evens(8)

def EvenNums(num):
    if num != 2:
        print(num)

    if num == 2:
        return num
    else:
        return EvenNums(num - 2)


print(EvenNums(8))