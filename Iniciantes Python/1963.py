value1, value2 = input().split()
value1 = float(value1)
value2 = float(value2)

if value1 == value2:
    print('0.00%')
else:
    print('{:.2f}%'.format((value2/value1)*100-100))
