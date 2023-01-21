codigo, number, valor = input().split()
codigo = int(codigo)
number = int(number)
valor = float(valor)

codigo2, number2, valor2 = input().split()
codigo2 = int(codigo2)
number2 = int(number2)
valor2 = float(valor2)

print('VALOR A PAGAR: R$ {:.2f}'.format(number*valor + number2*valor2))
