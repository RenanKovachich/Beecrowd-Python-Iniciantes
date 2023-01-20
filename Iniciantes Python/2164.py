import math
n = int(input())

part1 = math.pow((1+math.sqrt(5))/2.0, n)
part2 = math.pow((1-math.sqrt(5))/2.0, n)
valor = (part1 - part2) / math.sqrt(5)

print('{:.1f}'.format(valor))
