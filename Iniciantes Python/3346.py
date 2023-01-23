f1, f2 = map(float, input().split())

print('{:.6f}'.format((100+f1)*(f2/100+1)-100))
