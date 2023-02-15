n = int(input())
soma = 0.0
for i in range(1, n+1):
    a = list(map(float, input().split()))
    soma += a[0]/a[1]

if soma <= 1.0:
    print('OK')
else:
    print('FAIL')
    