#Aumento de Salário
sal = float(input())
if (sal >= 0) and (sal <= 400):
    print('Novo salario: {:.2f}'.format(sal*1.15))
    print('Reajuste ganho: {:.2f}'.format(sal*0.15))
    print('Em percentual: 15 %')
elif (sal >= 400.01) and (sal <= 800):
    print('Novo salario: {:.2f}'.format(sal * 1.12))
    print('Reajuste ganho: {:.2f}'.format(sal * 0.12))
    print('Em percentual: 12 %')
elif (sal >= 800.01) and (sal <= 1200):
    print('Novo salario: {:.2f}'.format(sal * 1.10))
    print('Reajuste ganho: {:.2f}'.format(sal * 0.10))
    print('Em percentual: 10 %')
elif (sal >= 1200.01) and (sal <= 2000):
    print('Novo salario: {:.2f}'.format(sal * 1.07))
    print('Reajuste ganho: {:.2f}'.format(sal * 0.07))
    print('Em percentual: 7 %')
else:
    print('Novo salario: {:.2f}'.format(sal * 1.04))
    print('Reajuste ganho: {:.2f}'.format(sal * 0.04))
    print('Em percentual: 4 %')
