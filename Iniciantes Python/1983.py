n = int(input())
nota = 0
m = 0
notas = []
matriculas_notas = []
for i in range(n):
    m, nota = input().split()
    m = int(m)
    nota = float(nota)
    notas.append(nota)
    matriculas_notas.extend((m, nota))

termo = matriculas_notas.index(max(notas))

if max(notas) >= 8:
    print(matriculas_notas[termo-1])
else:
    print('Minimum note not reached')
