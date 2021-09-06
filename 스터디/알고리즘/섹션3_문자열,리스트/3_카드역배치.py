import sys
for tc in range(1, 6):
    sys.stdin=open(f'./섹션3_입출력/3. 카드 역배치/in{tc}.txt', "r")
    card = list(range(21))
    for t in range(10):
        a, b = map(int, input().split())
        change = card[a:b + 1]
        change = change[::-1]
        i = 0
        for id in range(a, b+1):
            card[id] = change[i]
            i += 1
    result = card[1:]
    print('#{}'.format(tc), end=' ')
    for r in result:
        print('{}'.format(r), end=' ')
    print()
