number = int(input())

for x in range(number):
    hero, newton = input().split()

    if hero == 'Thor':
        print('Y')
    else:
        print('N')
        