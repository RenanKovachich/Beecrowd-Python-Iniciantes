matrix = []
operation = str(input())

for i in range(12):
    row = []

    for j in range(12):
        number = float(input())
        row.append(number)
    matrix.append(row)

if operation == 'S':
    sum = 0
    c = 11
    for l in range(11,0,-1):
        for k in range(0,c):
            sum += matrix[l][k]
        c -= 1
    print('{:.1f}'.format(sum))

elif operation == 'M':
    sum = 0
    c = 11
    c2 = 0
    for l in range(11,0,-1):
        for k in range(0,c):
            sum += matrix[l][k]
            c2 += 1
        c -= 1
    average = sum/c2
    print('{:.1f}'.format(average))
