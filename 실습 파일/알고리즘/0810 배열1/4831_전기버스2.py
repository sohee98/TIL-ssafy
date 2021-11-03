import sys
sys.stdin = open("4831sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    CHARGE = list(map(int, input().split()))

    #1 k=5, N=10, M=4 [1, 3, 9]
    # curP = 0
    # cnt = 0
    # while curP < N:
    #     nextP = curP + K
    #     if nextP >= N:
    #         break
    #
    #     if nextP not in CHARGE:
    #         while curP < nextP and nextP not in CHARGE:
    #             nextP -= 1
    #
    #         if curP == nextP:
    #             cnt = 0
    #             break
    #     else:
    #         cnt += 1
    #         curP = nextP


        # if nextP in CHARGE:     #충전기가 있나?
        #     cnt += 1
        #     curP = nextP
        # else:   # nextP의 값을 하나씩 빼면서 충전기가 있는지 확인
        #     while curP < nextP and nextP not in CHARGE:
        #         nextP -= 1
        #     if curP == nextP:
        #         cnt = 0
        #         break
        #     else:       #if nextP in CHARGE:
        #         cnt += 1
        #         curP = nextP


    #2 [4, 7, 9, 14, 17] k=5
    CHARGE.insert(0, 0)     # [0, 4, 7, 9, 14, 17]
    CHARGE.append(N)        # [0, 4, 7, 9, 14, 17, 20]
    lastP = 0
    cnt = 0
    for i in range(1, len(CHARGE)):
        # 충전기 사이의 거리를 확인한다.
        if CHARGE[i] - CHARGE[i-1] > K:
            cnt = 0
            break

        # i번째에 있는 충전기에서 충전여부를 결정한다.
        if CHARGE[i] > lastP + K:
            lastP = CHARGE[i-1]
            cnt += 1

    print('#{} {}'.format(t, cnt))
