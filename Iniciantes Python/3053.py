n = int(input())
lista = ['A', 'B', 'C']
k = input()

for c in range(n):
    i = int(input())
    if i == 1:
        aux1 = lista[0]
        aux2 = lista[1]
        lista[0] = aux2
        lista[1] = aux1
    if i == 2:
        aux2 = lista[1]
        aux3 = lista[2]
        lista[1] = aux3
        lista[2] = aux2
    if i == 3:
        aux1 = lista[0]
        aux3 = lista[2]
        lista[0] = aux3
        lista[2] = aux1

j = lista.index(k)
if j == 0:
    print('A')
elif j == 1:
    print('B')
elif j == 2:
    print('C')