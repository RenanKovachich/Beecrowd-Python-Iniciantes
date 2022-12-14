i = True
soma = 0
n = 0
while i:
    age = int(input())
    if age > 0:
        soma += age
        n += 1
    else:
        i = False
print('{:.2f}'.format(soma / n))
