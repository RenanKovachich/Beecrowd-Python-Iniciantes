while True:
    try:
        n = int(input())
    except EOFError:
        break

    nums = list(map(int, input().split()))

    if n == 1:
        print(nums[0])
        continue

    rangel = 0
    gugu = sum(nums)
    for num in nums:
        prev = abs(gugu - rangel)
        rangel += num
        gugu -= num
        curr = abs(gugu - rangel)
        if prev < curr:
            print(prev)
            break
