t = int(input())
for i in range(1, t+1):
    tipo = input()
    values = [int(x) for x in input().split()]
    r = values[0]
    g = values[1]
    b = values[2]
    p = 0.3 * r + 0.59 * g + 0.11 * b
    if tipo == 'min':
        print('Caso #{}: {}'.format(i, min(values)))
    elif tipo == 'max':
        print('Caso #{}: {}'.format(i, max(values)))
    elif tipo == 'eye':
        print('Caso #{}: {}'.format(i, round(p - 0.5)))
    elif tipo == 'mean':
        print('Caso #{}: {}'.format(i, round(((r+g+b)/3) - 0.5)))
