jogos = 0
inter = 0
gremio = 0
empate = 0
continuar = True

while continuar:
    linha = [int(x) for x in input().split()]
    x = int(linha[0])
    y = int(linha[1])

    if x > y:
        inter += 1
        jogos += 1
        while True:
            print('Novo grenal (1-sim 2-nao)')
            msg = int(input())
            if msg == 1:
                continuar = True
                break
            elif msg == 2:
                continuar = False
                break
    elif x == y:
        empate += 1
        jogos += 1
        while True:
            print('Novo grenal (1-sim 2-nao)')
            msg = int(input())
            if msg == 1:
                continuar = True
                break
            elif msg == 2:
                continuar = False
                break
    else:
        gremio += 1
        jogos += 1
        while True:
            print('Novo grenal (1-sim 2-nao)')
            msg = int(input())
            if msg == 1:
                continuar = True
                break
            elif msg == 2:
                continuar = False
                break
print('{} grenais'.format(jogos))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))
if inter > gremio:
    print('Inter venceu mais')
elif inter < gremio:
    print('Gremio venceu mais')
elif inter == gremio:
    print('Nao houve vencedor')
