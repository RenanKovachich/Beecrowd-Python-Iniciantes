n = int(input())
while n > 0:
    x = list(map(int, input().split()))
    a = sorted(x)
    menor, maior = a[n-1] + a[n], a[n-1] + a[n]
    for i in range(n):
        b = a[i] + a[2*n - i - 1]
        if b < menor:
            menor = b
        elif b > maior:
            maior = b
    print('{} {}'.format(maior, menor))
    n = int(input())
