while True:
    try:
        horas, minutos = input().split(':')
        horas = int(horas)
        minutos = int(minutos)
        tempo_total = horas*60+minutos

        atraso = (480 - tempo_total) - 60

        if atraso >= 0:
            print('Atraso maximo: 0')
        elif atraso < 0:
            print('Atraso maximo: {}'.format(abs(atraso)))
    except EOFError:
        break
