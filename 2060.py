n = int(input())

numero = input().split()
numeros = []
for j in numero:
    numeros.append(int(j))

mult2, mult3, mult4, mult5 = 0, 0, 0, 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        mult2 += 1
    if numeros[i] % 3 == 0:
        mult3 += 1
    if numeros[i] % 4 == 0:
        mult4 += 1
    if numeros[i] % 5 == 0:
        mult5 += 1

print('{} Multiplo(s) de 2'.format(mult2))
print('{} Multiplo(s) de 3'.format(mult3))
print('{} Multiplo(s) de 4'.format(mult4))
print('{} Multiplo(s) de 5'.format(mult5))
