n = int(input())

for i in range(n):
    linha = [int(num) for num in input().split()]
    x = min(linha)
    y = max(linha)

    soma = 0
    for num in range(x+1, y):
        if num % 2 == 1:
            soma += num

    print(soma)
    