value1 = int(input())
value2 = int(input())
count = 0
j = 1
while value2 <= value1:
    value2 = int(input())

count = value1
j = 1
aux = count
times = 0
while aux < value2:
    count = count + j
    aux = count + aux
    times += 1

print(times+1)
