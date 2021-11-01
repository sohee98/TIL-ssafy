def solve(n, c, sumV):      # n-재료수, c-칼로리합, sumV-점수합
    global maxV
    if c > L:
        return
    if sumV > maxV:
        maxV = sumV
    if n == N:
        return

    solve(n + 1, c+calory[n], sumV+score[n])
    solve(n + 1, c, sumV)

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    score = []
    calory = []
    for _ in range(N):
        T, K = map(int, input().split())    # T-점수, K-칼로리
        score.append(T)
        calory.append(K)
    maxV = 0
    solve(0, 0, 0)
    print('#{} {}'.format(tc, maxV))