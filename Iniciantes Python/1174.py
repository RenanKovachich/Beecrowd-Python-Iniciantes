contador = 0
while contador < 100:
    number = float(input())
    if number > 10:
        contador += 1
    else:
        print('A[{}] = {}'.format(contador, number))
        contador += 1
