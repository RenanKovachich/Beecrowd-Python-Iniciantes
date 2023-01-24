n = int(input())
saques = 0
bloqueio = 0
ataque = 0

pontos_saques = 0
pontos_bloqueio = 0
pontos_ataque = 0

for i in range(n):
    nome = input()
    s1, b1, a1 = [int(x) for x in input().split()]
    saques += s1
    bloqueio += b1
    ataque += a1

    s2, b2, a2 = [int(y) for y in input().split()]
    pontos_saques += s2
    pontos_bloqueio += b2
    pontos_ataque += a2


print('Pontos de Saque: {:.2f} %.'.format((pontos_saques/saques)*100))
print('Pontos de Bloqueio: {:.2f} %.'.format((pontos_bloqueio/bloqueio)*100))
print('Pontos de Ataque: {:.2f} %.'.format((pontos_ataque/ataque)*100))
