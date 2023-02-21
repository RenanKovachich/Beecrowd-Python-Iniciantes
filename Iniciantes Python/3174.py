n = int(input())
total = bonecos = arquitetos = musicos = desenhistas = 0
for i in range(n):
    e, g, h = input().split(' ')
    h = int(h)
    if g == 'bonecos':
        bonecos += h
    elif g == 'arquitetos':
        arquitetos += h
    elif g == 'musicos':
        musicos += h
    else:
        desenhistas += h
total = (bonecos // 8) + (arquitetos // 4) + (musicos // 6) + (desenhistas // 12)
print(total)
