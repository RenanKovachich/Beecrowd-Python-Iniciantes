while True:
    try:
        def min_time(entrada1, entrada2, saida1, saida2, linha1, linha2):
            if linha1:
                c1, c2 = linha1[0], linha2[0]
                a = c1[0] + min(entrada1, entrada2 + c2[1])
                b = c2[0] + min(entrada2, entrada1 + c1[1])
                return min_time(a, b, saida1, saida2, linha1[1:], linha2[1:])
            else:
                return min(entrada1 + saida1, entrada2 + saida2)


        n = input()
        n = int(n[0])
        if n == 0:
            break

        entrada = [int(x) for x in input().split()]
        tempo1 = [int(x) for x in input().split()]
        tempo2 = [int(x) for x in input().split()]
        transicao1 = [1000000] + [int(x) for x in input().split()]
        transicao2 = [1000000] + [int(x) for x in input().split()]
        saida = [int(x) for x in input().split()]
        linha1 = list(zip(tempo1, transicao1))
        linha2 = list(zip(tempo2, transicao2))
        print(min_time(entrada[0], entrada[1], saida[0], saida[1], linha1, linha2))

    except EOFError:
        break
