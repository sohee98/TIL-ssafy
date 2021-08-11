ARR = [[0]*5 for _ in range(3)]
for i in range(3):
    ARR[i] = list(map(int, input().split()))
print(ARR)

N = len(ARR)
M = len(ARR[0])

# 행 우선 조회
for i in range(N):
    for j in range(M):
        print(ARR[i][j])

# i번째 행의 합을 구해라
for i in range(N):
    sumV = 0
    for j in range(M):
        sumV += ARR[i][j]
    print(sumV)

# 열 우선 조회
for i in range(M):
    for j in range(N):
        print(ARR[j][i])

# i번째 열의 합을 구해라
for i in range(M):
    sumV = 0
    for j in range(N):
        sumV += ARR[j][i]
    print(sumV)

## 지그재그
# 0번째
for i in range(N):
    print(ARR[0][i])
# 1번째
for i in range(N-1, -1, -1):
    print(ARR[1][i])
# 전체
for i in range(N):
    if i%2==0:
        for j in range(M-1):  # => j
            print(ARR[i][j])
    else:
        # for j in range(M-1, -1, -1):     # => M-1-j
        #     print(ARR[i][j])
        for j in range(M-1):
            print(ARR[i][M-1-j])


## 상하좌우
dcol = [0, 0, -1, 1]
drow = [-1, 1, 0, 0]

for mode in range(4):
    newRow = i + drow[mode]
    newCol = j + dcol[mode]
    print(ARR[newRow][newCol])

# 행우선
for i in range(N):
    for j in range(M):
        for mode in range(4):
            newRow = i + drow[mode]
            newCol = j + dcol[mode]
            if 0 <= newRow < N and 0 <= newCol < M:
                print(ARR[newRow][newCol])


