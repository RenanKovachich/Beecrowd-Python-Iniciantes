lista = []
for x in range(100):
    num = int(input())
    lista.append(num)

ordenada = sorted(lista, reverse=True)
pos = ordenada[0]

print(ordenada[0])
print(lista.index(pos)+1)
