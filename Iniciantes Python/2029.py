while True:
    try:
        v = float(input())
        d = float(input())
        pi = 3.14
        r = d / 2

        h = v / (pi * r**2)
        a = pi * r * r

        print('ALTURA = {:.2f}'.format(h))
        print('AREA = {:.2f}'.format(a))
    except EOFError:
        break
