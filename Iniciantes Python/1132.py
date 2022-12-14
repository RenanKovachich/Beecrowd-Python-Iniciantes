x = int(input())
y = int(input())
soma = 0
if y > x:
    for w in range(x, y+1):
        if w % 13 != 0:
            soma += w
elif y < x:
    for q in range(y, x+1):
        if q % 13 != 0:
            soma += q
print(soma)
