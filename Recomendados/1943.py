k = int(input())
top1 = [1]
top3 = [2, 3]
top5 = [4, 5]
top10 = [6, 7, 8, 9, 10]
top25 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
top50 = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

if k in top1:
    print("Top 1")
elif k in top3:
    print("Top 3")
elif k in top5:
    print("Top 5")
elif k in top10:
    print("Top 10")
elif k in top25:
    print("Top 25")
elif k in top50:
    print("Top 50")
else:
    print("Top 100")
