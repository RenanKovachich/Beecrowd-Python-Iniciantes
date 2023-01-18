n, m = input().split()
n = int(n)
m = int(m)

for x in range(m):
    msg = input()
    if msg == 'fechou':
        n += 1
    elif msg == 'clicou':
        n -= 1

print(n)
