n = int(input())
for i in range(n):
    numbers = list(map(int, input().split()))
    tomadas = sum(numbers[1:]) - numbers[0] + 1
    print(tomadas)
