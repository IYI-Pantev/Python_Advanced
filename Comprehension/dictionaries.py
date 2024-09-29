point = {'x': 1, 'y': 2}
point['z'] = 20

print(point.get('a'))

for key, vale in point.items():
    print(key, ':', vale)

items = {x: x*3 for x in range(5, 12)}
print(items)
