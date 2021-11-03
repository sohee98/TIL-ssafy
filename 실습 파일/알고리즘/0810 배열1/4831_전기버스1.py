import sys
sys.stdin = open("4831sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    CHARGE = list(map(int, input().split()))

    cnt = 0
    CHARGE_1 = [0, *CHARGE, N, 100]
    chargeI = 0
    for i in range(1, len(CHARGE)+1):
        now = CHARGE_1[i] - CHARGE_1[chargeI]
        next = CHARGE_1[i+1] - CHARGE_1[i]
        next2 = CHARGE_1[i+2] - CHARGE_1[i]
        if next > K:
            cnt = 0
            break
        else:
            if now == K or now + next > K:
                cnt += 1
                chargeI = i
            if next2 <= K:
                continue
    print('#{} {}'.format(t, cnt))