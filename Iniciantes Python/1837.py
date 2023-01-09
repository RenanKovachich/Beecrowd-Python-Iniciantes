numeros = input().split()
n1, n2 = numeros
n1, n2 = int(n1), int(n2)

for r in range(abs(n2)):
    if (n1 - r) % n2 == 0:
        q = int((n1 - r) / n2)
        break
print(q, r)
