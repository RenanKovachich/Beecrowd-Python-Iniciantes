contador = 0
lista = []
while contador < 20:
    number = int(input())
    lista.append(number)
    if contador == 19:
        print('N[0] = {}'.format(lista[19]))
        print('N[1] = {}'.format(lista[18]))
        print('N[2] = {}'.format(lista[17]))
        print('N[3] = {}'.format(lista[16]))
        print('N[4] = {}'.format(lista[15]))
        print('N[5] = {}'.format(lista[14]))
        print('N[6] = {}'.format(lista[13]))
        print('N[7] = {}'.format(lista[12]))
        print('N[8] = {}'.format(lista[11]))
        print('N[9] = {}'.format(lista[10]))
        print('N[10] = {}'.format(lista[9]))
        print('N[11] = {}'.format(lista[8]))
        print('N[12] = {}'.format(lista[7]))
        print('N[13] = {}'.format(lista[6]))
        print('N[14] = {}'.format(lista[5]))
        print('N[15] = {}'.format(lista[4]))
        print('N[16] = {}'.format(lista[3]))
        print('N[17] = {}'.format(lista[2]))
        print('N[18] = {}'.format(lista[1]))
        print('N[19] = {}'.format(lista[0]))
        contador += 1
    else:
        contador += 1
