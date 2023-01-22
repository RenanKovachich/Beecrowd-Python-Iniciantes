while True:
    n, xp = [int(x) for x in input().split()]
    if n == 0 and xp == 0:
        break
    else:
        print(n*xp)
