number = int(input())
N = [] 
for i in range(1000):
    j = 0
    while j < number:
        N.append(j)
        j = j + 1
    print('N[{0}] = {1}'.format(i,N[i]))
