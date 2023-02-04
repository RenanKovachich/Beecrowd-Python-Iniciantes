n = int(input())
for i in range(n):
    q = bin(int(input()))
    q = q[2:]
    m = aux = 0
    for j in q:
        if j == '1':
            aux += 1
        else:
            aux = 0
        if aux > m:
            m = aux
    print(m)
