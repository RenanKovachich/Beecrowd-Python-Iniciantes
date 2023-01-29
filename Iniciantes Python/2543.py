while True:
    try:
        n, I = [int(x) for x in input().split()]
        cs = 0
        for c in range(n):
            i, j = [int(x) for x in input().split()]
            if i == I and j == 0:
                cs += 1

        print(cs)
    except EOFError:
        break
