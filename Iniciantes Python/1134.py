continuar = True
alcool = 0
gasolina = 0
diesel = 0
while continuar:
    num = int(input())
    if num == 1:
        alcool += 1
    elif num == 2:
        gasolina += 1
    elif num == 3:
        diesel += 1
    elif num == 4:
        continuar = False
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))
