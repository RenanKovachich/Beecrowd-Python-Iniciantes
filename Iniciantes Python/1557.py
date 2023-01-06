while True:
    n = int(input())
    if n == 0:
        break

    matriz = list()

    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)

    matriz[0][0] = 1
    for i in range(0, n):
        if i >= 1:
            matriz[i][0] = matriz[i - 1][0] * 2
        for j in range(1, n):
            matriz[i][j] = matriz [i][j - 1] * 2

    T = len(str(matriz[n-1][n-1]))
    for i in range(n):
        for j in range(n):
            matriz[i][j] = str(matriz[i][j])
            while len(matriz[i][j]) < T:
                matriz[i][j] = ' ' + matriz[i][j]
        M = ' '.join(matriz[i])

        print(M)
    print()
