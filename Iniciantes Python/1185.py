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
    c = 12
    for l in range(0, 11):
        c -= 1
        for k in range(0, c):
            sum += matrix[l][k]

    print('{:.1f}'.format(sum))
elif operation == 'M':
    sum = 0
    c = 12
    c2 = 0
    for l in range(0, 11):
        c -= 1
        for k in range(0, c):
            sum += matrix[l][k]
            c2 += 1
        
    average = sum/c2
    print('{:.1f}'.format(average))
    
