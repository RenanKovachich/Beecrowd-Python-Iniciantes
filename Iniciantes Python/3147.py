h, e, a, o, w, x = map(int, input().split())
heax = h + e + a + x
ow = o + w
if heax >= ow:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')
