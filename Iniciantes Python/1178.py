number = round(float(input()), 4)
lista = []
for i in range(100):
    lista.append(number)
    number = number/2
    print('N[{}] = {:.4f}'.format(i, lista[i]))
    
