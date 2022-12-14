continuar = True
j = 0
while continuar:
    linha = [int(x) for x in input().split()]
    n1 = int(linha[0])
    n2 = int(linha[1])

    if 1 < n1 < 20 and n1 < n2 < 1000000:
        for x in range(1, n2+1):

            if x % n1 == 0:
                print(x, end='\n')
            else:
                print(x, end=' ', flush=True)
        continuar = False
    else:
        continuar = False
