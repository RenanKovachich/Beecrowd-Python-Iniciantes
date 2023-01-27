while True:
    try:
        m = int(input())
        n = c = 0
        for i in range(m):
            m1, m2 = [int(x) for x in input().split()]
            c += m2
            n += m1*m2

        final = n/(c*100)
        print('{:.4f}'.format(final))

    except EOFError:
        break
