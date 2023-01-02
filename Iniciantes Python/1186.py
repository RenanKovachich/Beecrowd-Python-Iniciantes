matriz = []
operacao = str(input())

for i in range(12):
    linha = []

    for j in range(12):
        numeros = float(input())
        linha.append(numeros)
    matriz.append(linha)

if operacao == 'S':
    sum = 0
    c = 1
    for l in range(11, 0, -1):
        for k in range(c, 12):
            sum += matriz[l][k]
        c += 1
    print('{:.1f}'.format(sum))
elif operacao == 'M':
    sum = 0
    c = 1
    c2 = 0
    for l in range(11, 0, -1):
        for k in range(c, 12):
            sum += matriz[l][k]
            c2 += 1
        c += 1
    print('{:.1f}'.format(sum/c2))
    
