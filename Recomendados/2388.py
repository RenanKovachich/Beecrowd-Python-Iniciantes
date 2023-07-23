n = int(input())
count = 0
for i in range(n):
    t, v = map(int, input().split())
    count += t*v
    
print(count)
