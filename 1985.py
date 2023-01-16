n = int(input())
total = 0
for i in range(n):
    codigo, x = input().split()
    codigo = int(codigo)
    x = int(x)
    if codigo == 1001:
        total += 1.50 * x
    elif codigo == 1002:
        total += 2.5 * x
    elif codigo == 1003:
        total += 3.5 * x
    elif codigo == 1004:
        total += 4.5 * x
    elif codigo == 1005:
        total += 5.5 * x

print('{:.2f}'.format(total))
