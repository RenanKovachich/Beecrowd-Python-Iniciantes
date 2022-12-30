x = 0
par = []
impar = []
for j in range(15):
    number = int(input())
    if number % 2 == 0:
        par.append(number)
        print('par[{}] = {}'.format(j, par[j]))
    else:
        impar.append(number)
        print('impar[{}] = {}'.format(j, impar[j]))

    
        
