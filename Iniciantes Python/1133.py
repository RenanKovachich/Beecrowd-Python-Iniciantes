x = int(input())
y = int(input())

if x > y:
    for q in range(y+1, x):
        if q % 5 == 2 or q % 5 == 3:
            print(q)
elif x < y:
    for f in range(x+1, y):
        if f % 5 == 2 or f % 5 == 3:
            print(f)
