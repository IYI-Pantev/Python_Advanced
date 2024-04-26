numbers = [int(x) for x in input().split(' ')]
print(numbers)

positives = [x for x in numbers if x > 0]
negatives = [x for x in numbers if x < 0]
print(sum(positives))
print(sum(negatives))

if abs(sum(negatives)) > sum(positives):
    print('The Negatives are stronger')
else:
    print('The Positives are stronger')
