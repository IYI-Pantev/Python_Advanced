n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input().split(", "))

print([int(num) for sublist in matrix for num in sublist])
