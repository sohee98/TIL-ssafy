import sys
sys.stdin = open(f'5189sample_input.txt', "r")

def solve(i, sumV):      # i:현재 위치, sumV:합
    global minV
    if sum(visited) == N:
        sumV += ARR[i][0]
        if sumV < minV:
            minV = sumV
        return
    for j in range(1, N):
        if not visited[j]:      # i번에서 j번으로 이동
            visited[j] = 1
            solve(j, sumV + ARR[i][j])
            visited[j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    visited[0] = 1
    minV = 999
    solve(0, 0)
    print("#{} {}".format(tc, minV))
