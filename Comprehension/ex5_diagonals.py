n = int(input())
matrix = [[int(x)
           for x in input().split(', ')
           ] for _ in range(n)
          ]
# items = [1, 2, 3]
print([matrix[i][i] for i in range(n)])
# print(list(reversed(items)))
reverse = [list(reversed(sublist)) for sublist in matrix]
print([reverse[i][i] for i in range(n)])
