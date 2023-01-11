number = int(input())
msg = input().split()

for i in range(number):
    msg[i] = int(msg[i])

minimo = min(msg)
resultado = msg.index(minimo) + 1

print(resultado)
