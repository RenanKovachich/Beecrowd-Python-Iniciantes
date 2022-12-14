while True:
    linha = [int(num) for num in input().split()]
    x = int(linha[0])
    y = int(linha[1])

    if x == 0 or y == 0:
        break
    elif x > 0 and y > 0:
        print('primeiro')
    elif x < 0 < y:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 > y:
        print('quarto')
