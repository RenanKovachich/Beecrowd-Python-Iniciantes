t = int(input())

for i in range(t):
    b = int(input())
    ai, di, li = [int(x) for x in input().split()]  # Dabriel
    ai2, di2, li2 = [int(y) for y in input().split()]  # Guarte
    totalDabriel = (ai + di) / 2
    totalGuarte = (ai2 + di2) / 2

    if li % 2 == 0:
        totalDabriel += b
        if li2 % 2 == 0:
            totalGuarte += b
    elif li2 % 2 == 0:
        totalGuarte += b
        if li % 2 == 0:
            totalDabriel += b

    if totalDabriel > totalGuarte:
        print('Dabriel')
    elif totalDabriel == totalGuarte:
        print('Empate')
    else:
        print('Guarte')
