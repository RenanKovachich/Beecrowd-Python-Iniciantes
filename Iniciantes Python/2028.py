x = 1
while 1:
    try:
        n = 1
        a = int(input())

        for i in range(a + 1):
            n += i

        if n == 1:
            print('Caso %d: %d numero' % (x, n))
        else:
            print('Caso %d: %d numeros' % (x, n))

        if a == 0:
            print(0)
        else:
            print(0, end=' ')

        for i in range(a + 1):
            for b in range(i):
                if i == a and b == a - 1:
                    print(i)
                else:
                    print(i, end=' ')

        print('')
        x += 1
    except EOFError:
        break
