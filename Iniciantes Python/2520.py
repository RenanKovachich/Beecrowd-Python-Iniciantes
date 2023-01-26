while True:
    try:
        n, m = [int(v) for v in input().split()]
        matriz = []
        for i in range(n):
            linha = [int(x) for x in input().split()]
            matriz.append(linha)

        linha_2 = 0
        col_2 = 0
        for k in range(len(matriz)):
            for l in range(len(matriz[k])):
                if matriz[k][l] == 2:
                    linha_2 = k + 1
                    col_2 = l + 1
        linha_1 = 0
        col_1 = 0
        for z in range(len(matriz)):
            for x in range(len(matriz[z])):
                if matriz[z][x] == 1:
                    linha_1 = z + 1
                    col_1 = x + 1

        passos = (abs(linha_2 - linha_1)) + (abs(col_2 - col_1))
        print(passos)

    except EOFError:
        break
