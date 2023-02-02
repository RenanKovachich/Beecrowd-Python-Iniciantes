n = int(input())
a, b = [int(x) for x in input().split()]

if a+b <= n:
    print('Farei hoje!')
else:
    print('Deixa para amanha!')
