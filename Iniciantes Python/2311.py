n = int(input())
for i in range(n):
    nome = input()
    gd = float(input())
    notas = sorted([float(x) for x in input().split()])
    del notas[0]
    del notas[-1]
    total = sum(notas)
    
    print('{} {:.2f}'.format(nome, total*gd))
