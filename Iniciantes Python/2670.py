predio = [int(input()) for andar in range(3)]
tempo = [predio[0] * 4 + predio[1] * 2, predio[0] * 2 + predio[2] * 2, predio[1] * 2 + predio[2] * 4]

tempo.sort()
print(tempo[0])
