code, qtd = input().split()
code = int(code)
qtd = int(qtd)

if code == 1:
    print('Total: R$ {:.2f}'.format(4.00*qtd))
elif code == 2:
    print('Total: R$ {:.2f}'.format(4.50*qtd))
elif code == 3:
    print('Total: R$ {:.2f}'.format(5.00*qtd))
elif code == 4:
    print('Total: R$ {:.2f}'.format(2.00*qtd))
elif code == 5:
    print('Total: R$ {:.2f}'.format(1.50*qtd))
