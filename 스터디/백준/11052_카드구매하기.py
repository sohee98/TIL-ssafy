N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
## dp[n] => n 1개 or 1,n-1 or 2,n-2 or .. i,n-i 중 최대값
dp = list(P)
dp[2] = max(dp[2], dp[1]*2)
for i in range(3, N+1):
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[i-j]+dp[j])
print(dp[N])

# 프린트 빨라짐
# import sys
# sys.stdout.write(str(dp[N]))

## 재귀 - 시간초과
# def pick(k, sumV):
#     global maxV
#     if k > N:
#         return
#     if k == N:
#         if sumV > maxV:
#             maxV = sumV
#         return
#     for i in range(1, N+1):
#         if k+i <= N:
#             pick(k+i, sumV+P[i])
# maxV = 0
# pick(0, 0)
# print(maxV)


