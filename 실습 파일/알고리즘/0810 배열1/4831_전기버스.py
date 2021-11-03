import sys
sys.stdin = open("4831sample_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int,input().split())
    num = list(map(int, input().split()))

    charge = 0
    n = K                                       # n : 현재 갈 수 있는 정류장 갯수 n = 3
    for i in range(1, N+1):                     # 1~N까지 정류장 반복
        n -= 1                                  # n-1 => 한 번 이동했으므로
        if i in num and i+n < N:                # 충전기 있는 정류장에 도착, 종점전에 충전할 곳 없을때

            if n == 0 or i+n not in num:        # 현재 n=0 혹은 앞으로 충전할 수 없다면 충전
                charge += 1
                n = K                           # 충전 했으므로 n = 3

        if n == 0 and i+n < N and i not in num:   # n=0이고 앞으로 충전기가 없고 종점전에 충전할 수 없으면 0
            charge = 0
            break
    print('#{} {}'.format(t, charge))

