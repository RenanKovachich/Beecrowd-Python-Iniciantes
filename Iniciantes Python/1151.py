# num = int(input())
# atual = 0
# i = 1
# anterior = 1
# seq = 0
# while i <= num:
#    print('%d' % seq, end="\n")
#    seq = atual + anterior
#    anterior = atual
#    atual = seq
#    i += 1

n = int(input())
v1 = [0]*n

for i in range(0, n):
    if i <= 1:
        v1[i] = i
    else:
        v1[i] = v1[i-1] + v1[i-2]

    if i == n-1:
        print('%d' % (v1[i]), end='')
    else:
        print('%d' % (v1[i]), end=' ')

print()
