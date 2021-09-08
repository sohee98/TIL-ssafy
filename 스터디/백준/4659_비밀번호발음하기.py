while True:
    pwd = input()
    if pwd == 'end':
        break
    V = ['a', 'e', 'i', 'o', 'u']
    ST = []
    i = 0
    isV = False
    result = True
    while i < len(pwd):
        ST.append(pwd[i])
        now = ST.pop(-1)
        if now in V:
            isV = True
        if len(ST)>=1:
            if now == ST[-1] and now not in ['e','o']:
                result = False
                break
        if len(ST)>=2:
            if now in V and ST[-1] in V and ST[-2] in V:
                result = False
                break
            if now not in V and ST[-1] not in V and ST[-2] not in V:
                result = False
                break
        ST.append(now)
        i += 1

    if result and isV:
        print('<{}> is acceptable.' .format(pwd))
    else:
        print('<{}> is not acceptable.' .format(pwd))

