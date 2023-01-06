while True:
    try:
        n = int(input())

        resultado = []

        col2 = n - 1
        for i in range(n):
            tmp = []
            for j in range(n):
                if j == col2:
                    tmp.append(2)
                    col2 -= 1
                else:
                    if i == j:
                        tmp.append(1)
                    else:
                        tmp.append(3)
            resultado.append(tmp)

        for i in range(n):
            tx = ''
            for j in range(n):
                tx += str(resultado[i][j])
            print(tx)
    except EOFError:
        break
       
