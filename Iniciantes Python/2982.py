n = int(input())
s = 0
for i in range(n):
    tc = input().split()
    t = tc[0]
    c = int(tc[1])

    if t == 'V':
        s += c
    else:
        s -= c

if s >= 0:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')