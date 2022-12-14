num = int(input())

if num % 2 == 0:
    num += 1
value = num
for x in range(num, num+10):
    print(value)
    value += 2
    if value >= num+11:
        break
