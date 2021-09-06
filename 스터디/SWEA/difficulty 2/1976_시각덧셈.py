T = int(input())
for tc in range(1, T+1):
    h1 , m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2
    if m1 + m2 >= 60:
        m -= 60
        h += 1
    if h > 12:
        h -= 12
    print('#{} {} {}'.format(tc, h, m))
