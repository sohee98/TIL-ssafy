## 못품
N = [list(map(int, input().split())) for _ in range(5)]
M = [list(map(int, input().split())) for _ in range(5)]

dic = {}
for i in range(5):
    for j in range(5):
        dic[N[i][j]] = (i, j)
lineX = []
lineY = []
bingo = 0
for i in range(5):
    for j in range(5):
        x = dic[M[i][j]]
        lineX.append(x[0])
        lineY.append(x[1])
        if len(lineX) >= 5:
            for a in range(len(lineX)):
                if lineX.count(lineX[a]) >= 5:
                    bingo += 1
                if lineX.count(lineY[a]) >= 5:
                    bingo += 1
