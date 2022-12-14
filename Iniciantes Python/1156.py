x = 1
soma = 0
for i in range(1, 40, 2):
    soma = float(soma + i/x)
    x = x * 2
print('{:.2f}'.format(soma))
