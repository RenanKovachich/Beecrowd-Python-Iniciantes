n = int(input())
lista = [int(x) for x in input().split()]
total = 1
for i in range(2, n):
    if lista[i] - lista[i-1] != lista[i-1] - lista[i-2]:
        total += 1
print(total)
