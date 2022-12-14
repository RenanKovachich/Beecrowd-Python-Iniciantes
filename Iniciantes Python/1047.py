#Tempo de Jogo com Minutos
hi, mi, hf, mf = map(int, input().split())

mi += hi*60
mf += hf*60

tempo = mf - mi
if tempo <= 0:
    tempo += 24*60

h = tempo // 60
m = tempo % 60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))