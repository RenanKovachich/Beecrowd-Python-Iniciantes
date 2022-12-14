while True:
    linha = [int(num) for num in input().split()]
    x = min(linha)
    y = max(linha)
    lista = []
    if x <= 0 or y <= 0:
        break
    for w in range(x, y+1):
        soma = lista.append(w)
        print(w, end=' ')
    print('Sum={}'.format((sum(range(x, y+1)))))
