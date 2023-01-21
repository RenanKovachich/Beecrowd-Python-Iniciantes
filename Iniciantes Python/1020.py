tempo = int(input())

anos = tempo // 365
tempo = tempo - anos*365
meses = tempo // 30
tempo = tempo - meses*30
dias = tempo

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
