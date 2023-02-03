total = 0
salida = 0
vuelta = 0
while True:
    msg = input().split()
    if msg[0] == 'ABEND':
        break
    elif msg[0] == 'SALIDA':
        total += int(msg[1])
        salida += 1
    elif msg[0] == 'VUELTA':
        total -= int(msg[1])
        vuelta += 1

print(total)
print(salida-vuelta)
