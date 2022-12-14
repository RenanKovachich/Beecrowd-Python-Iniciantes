num = int(input())
value = 1

if num == 1:
    print(value)
    value -= 1

for i in range(0, num):
    print(value)
    value += 2
    if value > num:
        break
