n = int(input())
while n != 0:
    n -= 1
    inp = input()
    if inp == "P=NP":
        print('skipped')
    else:
        a, b = inp.split('+')
        print(int(a)+int(b))
