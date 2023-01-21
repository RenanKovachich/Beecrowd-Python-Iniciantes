tempo = int(input())

horas = tempo // 3600
tempo = tempo - horas*3600
minutos = tempo // 60
tempo = tempo - minutos*60
segundos = tempo
print('{}:{}:{}'.format(horas, minutos, segundos))
