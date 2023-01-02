matriz = []
op = str(input())

for i in range(12):
    linha = []
    for j in range(12):
        numeros = float(input())
        linha.append(numeros)
    matriz.append(linha)

if op == 'S':
    sum = 0
    c1 = 1
    c2 = 11
    for l in range(11, 6, -1):
        for k in range(c1, c2):
            sum += matriz[l][k]
        c1 += 1
        c2 -= 1
    print('{:.1f}'.format(sum))
elif op == 'M':
    suma = 0
    c1 = 1
    c2 = 11
    c3 = 0
    for l in range(11, 6, -1):
        for k in range(c1, c2):
            c3 += 1
            sum += matriz[l][k]
        c1 += 1
        c2 -= 1
    print('{:.1f}'.format(sum/c3))
    
