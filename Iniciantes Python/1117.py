provas = 0
media = 0
while 2 > provas:
    nota = float(input())

    if 0 <= nota <= 10:
        media += nota
        provas += 1
    else:
        print('nota invalida')
print('media = {:.2f}'.format(media/2))
