quantidade_pares = 0
quantidade_impar = 0
quantidade_pos = 0
quantidade_neg = 0

for i in range(5):
    x = float(input())
    if x % 2 == 0:
        quantidade_pares += 1
    if x % 2 != 0:
        quantidade_impar += 1
    if x > 0:
        quantidade_pos += 1
    if x < 0:
        quantidade_neg += 1

print('{} valor(es) par(es)'.format(quantidade_pares))
print('{} valor(es) impar(es)'.format(quantidade_impar))
print('{} valor(es) positivo(s)'.format(quantidade_pos))
print('{} valor(es) negativo(s)'.format(quantidade_neg))
