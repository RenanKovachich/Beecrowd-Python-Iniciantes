temp = input().split()
t1, t2, t3 = temp

t1, t2, t3 = int(t1), int(t2), int(t3)

dif1 = t2 - t1
dif2 = t3 - t2

if t1 > t2:
    if t3 > t2:
        print(':)')
    else:
        if t2 - t3 < t1 - t2:
            print(':)')
        else:
            print(':(')

elif t1 < t2:
    if t3 < t2:
        print(':(')
    else:
        if t2 - t3 > t1 - t2:
            print(':(')
        else:
            print(':)')

else:
    if t3 > t1:
        print(':)')
    else:
        print(':(')
