n = int(input())
qntTotalCasas = n * n

if n % 2 == 0:
    a = qntTotalCasas // 2
    b = a
    print('{} casas brancas e {} casas pretas'.format(a, b))
else:
    a = (qntTotalCasas + 1) // 2
    b = a - 1
    print('{} casas brancas e {} casas pretas'.format(a, b))
