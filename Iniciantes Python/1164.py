num = int(input()) #Numero de termos
i = 0
while i < num:
    number = int(input())
    soma = 0
    for y in range(1, number):
        if number % y == 0 and number != y:
            soma = soma + y
    if soma == number:
        print('{} eh perfeito'.format(number))
        i += 1
    else:
        print('{} nao eh perfeito'.format(number))
        i += 1
