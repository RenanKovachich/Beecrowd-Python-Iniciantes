while True:
    n, m = input().split()
    n = int(n)
    m = int(m)

    if n == 0 and m == 0:
        break
    else:
        troco = m - n

        if troco > 200:
            print('impossible')
        elif troco == 200 or troco == 150 or troco == 120 or troco == 110 or troco == 105 or troco == 102 or troco == 70 \
                or troco == 60 or troco == 55 or troco == 52 or troco == 30 or troco == 25 or troco == 22 or troco == 15 or \
                troco == 12 or troco == 10 or troco == 7 or troco == 4:

            print('possible')
        else:
            print('impossible')
