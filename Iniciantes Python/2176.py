n = input()
value = 0

for i in n:
    if i == '1':
        value += 1

print('{}{}'.format(n, str(value % 2)))
