num = int(input())
total = 0
coelhos = 0
sapos = 0
ratos = 0

for x in range(num):
    numero, tipo = input().split()
    numero = int(numero)
    total += numero
    if tipo == 'C':
        coelhos += numero
    if tipo == 'R':
        ratos += numero
    if tipo == 'S':
        sapos += numero

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(coelhos*100/total))
print('Percentual de ratos: {:.2f} %'.format(ratos*100/total))
print('Percentual de sapos: {:.2f} %'.format(sapos*100/total))
