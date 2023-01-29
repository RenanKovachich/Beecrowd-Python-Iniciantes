while True:
    try:
        n = int(input())
        treino = []
        rec = []
        media = 0
        while n:
            n -= 1
            treino.append([int(x) for x in input().split()])
            if len(treino) == 1:
                media = treino[0][1]/treino[0][0]
                rec.append(1)
            else:
                if treino[-1][1] / treino[-1][0] > media:
                    media = treino[-1][1] / treino[-1][0]
                    rec.append(1)
                else:
                    rec.append(0)
        for i in range(len(rec)):
            if rec[i] == 1:
                print(i+1)

    except EOFError:
        break
