n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append([int(x) for x in input().split(", ")])

even = [[int(num) for num in input().split(", ") if int(num) % 2 == 0] for _ in range(n)]
print(even)
