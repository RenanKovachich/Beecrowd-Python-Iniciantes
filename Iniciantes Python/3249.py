def venceu_batalha(habilidades):
    return "CD" not in habilidades

n = int(input())
vitorias = 0

for _ in range(n):
    habilidades = input()
    if venceu_batalha(habilidades):
        vitorias += 1

print(vitorias)
