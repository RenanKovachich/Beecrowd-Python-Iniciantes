num1 = int(input())
num2 = int(input())
valor = 0
if num1 == num2:
    print(0)
    quit()
for x in range(num2 + 1, num1):
    if x % 2 != 0:
        valor += x
print(valor)
