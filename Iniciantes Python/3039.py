n = int(input())
carrinhos = bonecas = 0

while n > 0:
    nome, sexo = input().split()
    if sexo == 'F':
        bonecas += 1
    else:
        carrinhos += 1
    n -= 1

print(str(carrinhos) + " carrinhos")
print(str(bonecas) + ' bonecas')