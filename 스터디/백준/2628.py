N, M = map(int, input().split())    # 가로 세로
K = int(input())
cut = [[] for _ in range(2)]              # [[가로 번호], [세로 번호]]
for k in range(K):
    a, b = map(int, input().split())
    cut[a].append(b)
cut[0].append(M)
cut[1].append(N)
res = []
for i in range(2):
    cut[i].insert(0, 0)
    cut[i].sort()
    maxL = 0
    for j in range(len(cut[i])-1):
        l = cut[i][j+1] - cut[i][j]
        if l > maxL:
            maxL = l
    res.append(maxL)
print(res[0]*res[1])



