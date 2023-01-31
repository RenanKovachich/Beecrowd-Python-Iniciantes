lista = []

while True:
    try:
        lista.append(input())
    except EOFError:
        break

lista = set(lista)
print(len(lista))
