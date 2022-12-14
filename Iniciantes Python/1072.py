x = int(input())
value_in = 0
value_out = 0

for i in range(x):
    num = int(input())
    if 10 <= num < 25:
        value_in += 1
    else:
        value_out += 1
print('{} in'.format(value_in))
print('{} out'.format(value_out))
