entrada = list(map(int, input().split()))
titas = input()
tamanho = list(map(int, input().split()))

n, x = entrada[0], entrada[1]
t1, t2, t3 = tamanho[0], tamanho[1], tamanho[2]
muralhas = [x] * n
p, m, g = 0, 0, 0

for t in titas:
    if t == 'P':
        while muralhas[p] < t1:
            p += 1
        muralhas[p] -= t1
    elif t == 'M':
        while muralhas[m] < t2:
            m += 1
        muralhas[m] -= t2
    else:
        while muralhas[g] < t3:
            g += 1
        muralhas[g] -= t3

print(max([p, m, g])+1)
