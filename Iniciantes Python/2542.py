while True:
    try:
        n = int(input())  # Numeros de atributos de cada carta
        m, L = [int(x) for x in input().split()]  # Numero de cartas
        marcos = []
        leonardo = []
        for i in range(m):
            marcos_a = [int(x) for x in input().split()]
            marcos.append(marcos_a)
        for j in range(L):
            leonardo_a = [int(x) for x in input().split()]
            leonardo.append(leonardo_a)
        cm, cl = [int(x) for x in input().split()]
        marcos_final = marcos[cm-1]
        leonardo_final = leonardo[cl-1]
        a = int(input())

        if marcos_final[a-1] > leonardo_final[a-1]:
            print('Marcos')
        elif marcos_final[a-1] == leonardo_final[a-1]:
            print('Empate')
        else:
            print('Leonardo')
    except EOFError:
        break
