e, f, c = map(int, input().split())
g = e+f
resp = 0
while g >= c:
    resp += g // c
    g = g // c + g % c
print(resp)
