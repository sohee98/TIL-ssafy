# 못품
def queen(si, sj):
    global cnt
    for i in range(si, N):
        for j in range(sj, N):
            if not row_visited[i] and not col_visited[j] and not diag1_visited[i-j+N-1] and not diag2_visited[i+j]:
                row_visited[i] = 1
                col_visited[j] = 1
                diag1_visited[i-j+N-1] = 1
                diag2_visited[i+j] = 1
    if sum(row_visited)==N and sum(col_visited)==N:
        cnt += 1
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(N):
        for j in range(N):  # 시작점 i, j
            row_visited = [0] * N
            col_visited = [0] * N
            diag1_visited = [0] * (N * 2 - 1)  # \ => i-j+N-1 = 오른쪽 위부터 0
            diag2_visited = [0] * (N * 2 - 1)  # / => i+j = 왼쪽 위부터 0

            row_visited[i] = 1
            col_visited[j] = 1
            diag1_visited[i-j+N-1] = 1
            diag2_visited[i+j] = 1
            queen(i, j)
    print('#{} {}'.format(tc, cnt))


