a = 0
b = 1
L = []
n = int(input())
while n > len(L):
    p = a + b
    for j in range(b+1, p):
        L.append(j)
    a = b
    b = p
print(L[n-1])