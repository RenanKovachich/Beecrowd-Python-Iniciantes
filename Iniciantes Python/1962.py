n = int(input())

for x in range(n):
    age = int(input())

    if age > 2014:
        print('{} A.C.'.format(age - 2014))
    elif age < 2015:
        print('{} D.C.'.format(2015 - age))
