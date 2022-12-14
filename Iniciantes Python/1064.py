quantidade = 0
media = float()

for i in range(6):
    x = float(input())
    if x > 0.0:
        quantidade += 1
        media += x


print('{} valores positivos'.format(quantidade))
print('{:.1f}'.format(media/quantidade))
