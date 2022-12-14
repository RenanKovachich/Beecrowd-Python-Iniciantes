num = int(input())
for x in range(num):
    number = int(input())
    cont = 0
    i = 0
    while i <= number or cont < 2:
        i += 1
        z = number % i
        if z == 0:
            cont += 1
    if cont <= 2:
        print('{} eh primo'.format(number))
    else:
        print('{} nao eh primo'.format(number))
