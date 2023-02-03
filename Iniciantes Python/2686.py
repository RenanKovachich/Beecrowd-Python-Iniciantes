while True:
    try:
        m = float(input())
        if m <= 360:
            if m < 90 or m == 360:
                print('Bom Dia!!')
            elif m < 180:
                print('Boa Tarde!!')
            elif m < 270:
                print('Boa Noite!!')
            elif m < 360:
                print('De Madrugada!!')
            else:
                print('Bom Dia!!')

            if m >= 270:
                horas = ((m-270) * 4) / 60
            else:
                horas = ((m*4)/60) + 6
            minutos = (horas*60) % 60
            segundos = (minutos*60) % 60

            if segundos > 59:
                segundos = 0
                minutos += 1

            horas = int(horas)
            minutos = int(minutos)
            segundos = int(segundos)
            if horas > 9:
                if minutos > 9:
                    if segundos > 9:
                        print('{}:{}:{}'.format(horas, minutos, segundos))
                    else:
                        print('{}:{}:0{}'.format(horas, minutos, segundos))
                else:
                    if segundos > 9:
                        print('{}:0{}:{}'.format(horas, minutos, segundos))
                    else:
                        print('{}:0{}:0{}'.format(horas, minutos, segundos))
            else:
                if minutos > 9:
                    if segundos > 9:
                        print('0{}:{}:{}'.format(horas, minutos, segundos))
                    else:
                        print('0{}:{}:0{}'.format(horas, minutos, segundos))
                else:
                    if segundos > 9:
                        print('0{}:0{}:{}'.format(horas, minutos, segundos))
                    else:
                        print('0{}:0{}:0{}'.format(horas, minutos, segundos))
    except EOFError:
        break
