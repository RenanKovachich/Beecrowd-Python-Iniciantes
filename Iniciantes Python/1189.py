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
    c1 = 0
    c2 = 1
    for l in range(1, 11):
        for k in range(0, c2):
            sum += matriz[l][k]
        if l < 5:
            c2 += 1
        if l > 5:
            c2 -= 1
        
    print('{:.1f}'.format(sum))
    
elif op == 'M':
    sum = 0
    c1 = 0
    c2 = 1
    c3 = 0
    for l in range(1, 11):
        for k in range(0, c2):
            sum += matriz[l][k]
            c3 += 1
        if l < 5:
            c2 += 1
        if l > 5:
            c2 -= 1
            
    print('{:.1f}'.format(sum/c3))
