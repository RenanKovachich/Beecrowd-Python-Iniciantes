i = 2
while True:
    try:
        n = int(input())
        x = [int(k) for k in input().split()]
        sub = sum(x[i:]) - sum(x[:i])
        for j in range(2, len(x)):
            i += 1
            dif = sum(x[i:]) - sum(x[:i])
            if dif < 0:
                break
            sub = dif
        print(sub)
    except EOFError:
        break
        