import math


def solucao(a, b, c):
    return (b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


L, k, t1, t2, h = map(float, input().split())
if L > h:
    min_max = (h, h)
else:
    f = solucao(1, h+k * (t1 + t2), k * L * t1)
    if L < h:
        min_max = (f, f)
    else:
        min_max = (h, f)
print('{:.9f} {:.9f}'.format(min_max[0], min_max[1]))
