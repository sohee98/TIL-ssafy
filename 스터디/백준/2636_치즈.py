N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(*arr, sep='\n')

def find_up(i, j):  # 위쪽 부분
    for r in range(0, i):
        if arr[r][j]:
            return False
    return True
def find_down(i, j):    # 아래쪽 부분
    for r in range(i+1, N):
        if arr[r][j]:
            return False
    return True
def find_updown(i, j):  # 세로에서 위 or 아래가 다 0일 때
    if find_up(i, j) or find_down(i, j):
        return True
    return False

def find_side(i,j):  # 가로에서 왼쪽 or 오른쪽이 다 0일 때
    if sum(arr[i][:j]) == 0 or sum(arr[i][j+1:]) == 0:
        return True
    return False

def find_j(i, j):
    for n in range(1, M):  # n칸 왼쪽
        if 0 <= j-n < N:
            if arr[i][j-n] >= 1:
                break
            if find_updown(i, j-n):
                arr[i][j] = 2
                break
    for n in range(1, M):  # n칸 오른쪽
        if 0 <= j+n < N:
            if arr[i][j+n] >= 1:
                break
            if find_updown(i, j+n):
                arr[i][j] = 2
                break
    return

def find_i(i, j):
    for n in range(1, N):  # n칸 위
        if 0 <= i-n < N:
            if arr[i-n][j] >= 1:
                break
            if find_side(i-n, j):
                arr[i][j] = 2
                break
    for n in range(1, N):  # n칸 아래
        if 0 <= i+n < N:
            if arr[i+n][j] >= 1:
                break
            if find_side(i+n, j):
                arr[i][j] = 2
                break
    return

# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
# def find(i, j, curi, curj, visited):
#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]
#         if ni < 0 or ni > N or nj < 0 or nj > N:
#             arr[curi][curj] = 2
#             return
#         if arr[ni][nj] == 1 or visited[ni][nj]:
#             return
#         visited[ni][nj] = 1
#         find(ni, nj, curi, curj, visited)
#         visited[ni][nj] = 0


def find_cheese():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if find_side(i, j) or find_updown(i, j):    # 가로/세로에서 왼쪽 or 오른쪽이 다 0일 때
                    arr[i][j] = 2
                    continue
                if find_j(i, j) or find_i(i, j):            # 옆(왼쪽/오른쪽)의 위 or 아래가 다 0일 때
                    arr[i][j] = 2
                    break

                # visited = [[0]*M for _ in range(N)]
                # curi, curj = i, j
                # find(i, j, curi, curj, visited)

def melt():         # 2인 부분 0으로 바꾸기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                arr[i][j] = 0

def mySum(ARR):     # 2차원 배열 더하기
    result = 0
    for lst in ARR:
        result += sum(lst)
    return result

cnt = 0
while mySum(arr):
    cheese = mySum(arr)
    find_cheese()
    print('====================================')
    print(*arr, sep='\n')
    melt()
    cnt += 1
print(cnt)
print(cheese)