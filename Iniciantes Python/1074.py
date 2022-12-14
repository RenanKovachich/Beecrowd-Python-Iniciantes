x = int(input())

for x in range(0, x):
    x = int(input())
    if x % 2 == 0 and x > 0:
        print('EVEN POSITIVE')
    elif x % 2 != 0 and x > 0:
        print('ODD POSITIVE')
    elif x == 0:
        print('NULL')
    elif x % 2 == 0 and x < 0:
        print('EVEN NEGATIVE')
    elif x % 2 != 0 and x < 0:
        print('ODD NEGATIVE')
