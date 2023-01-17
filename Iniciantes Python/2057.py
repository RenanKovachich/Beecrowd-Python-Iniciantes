saida, tempo, fuso = input().split()
saida = int(saida)
tempo = int(tempo)
fuso = int(fuso)

decorer = (saida + tempo) + fuso
if decorer < 0:
    print(decorer+24)
elif decorer == 24:
    print(0)
elif decorer > 24:
    print(decorer-24)
else:
    print(decorer)
