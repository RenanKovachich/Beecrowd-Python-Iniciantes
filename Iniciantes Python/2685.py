while True:
    try:
        m = int(input())
        if (0 <= m < 90) or m == 360:
            print('Bom Dia!!')
        elif 180 > m >= 90:
            print('Boa Tarde!!')
        elif 270 > m >= 180:
            print('Boa Noite!!')
        else:
            print('De Madrugada!!')
    except EOFError:
        break
