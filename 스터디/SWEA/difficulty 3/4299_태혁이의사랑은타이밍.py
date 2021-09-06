T = int(input())
for tc in range(1, T + 1):
    D, H, M = map(int, input().split())
    if D > 11 or (D==11 and H >= 11) or (D==11 and H==11 and M >= 11):
        mi = M - 11
        ho = H - 11
        da = D - 11
        if mi < 0:      # 1시 5분 -> (1-11)+24 / (5-11)+60, h-1
            mi += 60
            ho -= 1
        if ho < 0:
            ho += 24
            da -= 1
        minute = da*24*60 + ho*60 + mi
    else:
        minute = -1

    print('#{} {}'.format(tc, minute))