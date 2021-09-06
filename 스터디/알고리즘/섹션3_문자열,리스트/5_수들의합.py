import sys
for i in range(1, 6):
    sys.stdin = open(f'./섹션3_입출력/5. 수들의 합/in{i}.txt', "r")
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(1, N-i):
            tmp = []
            for k in range(i, i+j+1):
                tmp.append(A[k])
            if sum(tmp) == M:
                cnt += 1
                break
            if sum(tmp) > M:
                break
    print(cnt)

