quantidade = 0

for i in range(5):
    if float(input()) % 2 == 0:
        quantidade += 1
print('{} valores pares'.format(quantidade))
