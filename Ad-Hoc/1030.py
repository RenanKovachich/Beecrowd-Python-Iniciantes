nc = int(input())
for i in range(1, nc+1):
    n, k = map(int, input().split())
    sobrevivente = 0
    for j in range(1, n+1):
        sobrevivente = (sobrevivente + k) % j

    print("Case {}: {}".format(i, sobrevivente+1))
