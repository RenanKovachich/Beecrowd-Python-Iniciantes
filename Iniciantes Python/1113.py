while True:
    linha = [int(num) for num in input().split()]
    x = int(linha[0])
    y = int(linha[1])

    if x == y:
        break
    elif x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
