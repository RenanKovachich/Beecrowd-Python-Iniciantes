sal = float(input())
if (sal>=0) and (sal<=2000):
    print('Isento')
elif (sal>2000) and (sal<=3000):
    conta = (sal - 2000.0)*0.08
    print('R$ {:.2f}'.format(conta))
elif (sal>3000.01) and (sal<= 4500):
    conta = (sal - 3000.0)*0.18 + (1000*0.08)
    print('R$ {:.2f}'.format(conta))
elif (sal>4500):
    conta = (sal-4500)*0.28 + (1500*0.18) + (1000*0.08)
    print('R$ {:.2f}'.format(conta))