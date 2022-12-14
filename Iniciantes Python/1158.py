j = 0
n = int(input())
while j < n:
    i = 0
    aux = 0
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    vector = []
    if x % 2 == 0:
        x += 1
    while i < y:
        vector.append(x)
        i += 1
        x += 2
    print(sum(vector))
    j += 1
