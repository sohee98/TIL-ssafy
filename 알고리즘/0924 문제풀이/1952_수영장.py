import sys
sys.stdin = open(f'1952sample_input.txt', "r")

# cost : 이전 달까지의 계산 결과, m : 현재 내가 보낼 결과
def calc(cost, m):
    global min_cost
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return
    # 1일권
    # calc(cost + d*month[m], m+1)
    # 1달권
    # calc(cost + m1, m+1)
    calc(cost + min(d * month[m], m1), m + 1)
    # 3달권
    calc(cost + m3, m+3)

T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    min_cost = y        # 1년치 비용이 현재의 최저 가격
    calc(0,1)
    print('#{} {}'.format(tc, min_cost))

########################################################

T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    dp = [0]*13     # 해당 월까지의 최소갑이 저장되어있음
    dp[1] = min(m1, month[1]*d)
    dp[2] = dp[1] + min(m1, month[2]*d)
    for i in range(3, 13):
                # 전달 + 3달치 / 1달치 / 1일권
        dp[i] = min(dp[i-3] + m3, dp[i-1] + m1, dp[i-1] + month[i]*d)
    print('#{} {}'.format(tc, min_cost))