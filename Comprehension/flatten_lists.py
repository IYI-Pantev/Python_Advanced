import sys
from io import StringIO

data_input = """1 2 3 |4 5 6 |  7  8"""
sys.stdin = StringIO(data_input)

matrix = [seq.split(' ') for seq in input().split("|")]
print(matrix)

flatten = [num for sublist in matrix for num in sublist if num.isdigit()]
print(flatten)
flatten.reverse()
print(" ".join(flatten))

