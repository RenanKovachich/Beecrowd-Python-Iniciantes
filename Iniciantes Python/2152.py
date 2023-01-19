c = int(input())
for i in range(c):
    h, m, o = input().split()
    msg = ''
    if (int(h) < 10) and (len(h) == 1):
        msg = '0' + h
    else:
        msg = h

    msg += ':'

    if (int(m) < 10) and (len(m) == 1):
        msg += '0' + m
    else:
        msg += m

    msg += ' - A porta '

    if o == '0':
        msg += 'fechou!'
    else:
        msg += 'abriu!'

    print(msg)
