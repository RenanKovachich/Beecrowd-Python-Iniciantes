while True:
    try:
        a, b = [int(x) for x in input().split()]
        print('%02d:%02d' % (a // 30, b // 6))
    except:
        break