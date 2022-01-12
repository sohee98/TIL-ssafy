dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    # c = 0
    # if arr[x][y] == 1:
    #     arr[x][y] += c
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #         if 0 <= nx < N and 0 <= ny < N:
    #             dfs(nx, ny)
    # c += 1
    global cnt

    if 0 <= x < N and 0 <= y < N:
        if arr[x][y] == 1:
            cnt += 1
            arr[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
        return False


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0  # 각 블록당 몇개냐
res = 0  # 몇 개의 블록이 나오느냐
result = []  # 밑에서 순서대로 출력하기 위해 리스트로 생성
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result.append(cnt)
            res += 1
            cnt = 0

result.sort()
print(res)
for a in result:
    print(a)