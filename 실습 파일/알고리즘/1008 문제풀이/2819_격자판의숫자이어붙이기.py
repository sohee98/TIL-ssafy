import sys
sys.stdin = open(f'2819sample_input.txt', "r")

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c, line):        # 좌표, line:만든숫자
    if len(line) == 7:
        if line not in ans:
            ans.append(line)
        return
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue
        dfs(nr, nc, line+arr[nr][nc])

T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = [input().split() for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            dfs(i, j, arr[i][j])
    print('#{} {}'.format(tc, len(ans)))