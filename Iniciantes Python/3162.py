import math

n = int(input())
ss = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    distancia = 500.0
    for j in range(n):
        if i != j:
            s, r = ss[i], ss[j]
            a, b, c = s[0] - r[0], s[1] - r[1], s[2] - r[2]
            diff = math.sqrt(a**2 + b**2 + c**2)
            if diff < distancia:
                distancia = diff
    if distancia <= 20:
        print('A')
    elif distancia <= 50:
        print('M')
    else:
        print('B')
