contador = 0
j = 0
while contador < 10:
    num = int(input())
    if num <= 0:
        print('X[{}] = 1'.format(j))
        j += 1
        contador += 1
    else:
        print('X[{}] = {}'.format(j, num))
        j += 1
        contador += 1
    
