while True:
    try:
        number = int(input())
        s = int(number/3)
        z = number - s

        matriz = [[0 for i in range(number)]for j in range(number)]

        for i in range(number):
            matriz[i][i] = 2
        j = 0
        for i in range(number-1, -1, -1):
            matriz[j][i] = 3
            j += 1

        for i in range(s, z):
            for j in range(s, z):
                matriz[i][j] = 1

        matriz[int(number/2)][int(number/2)] = 4

        for i in range(number):
            for j in range(number):
                print(matriz[j][i], end='')
            print()
        print()

    except EOFError:
        break