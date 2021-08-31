N, K = map(int, input().split())
stu_G = [0 for _ in range(7)]
stu_B = [0 for _ in range(7)]
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        stu_G[Y] += 1
    else:
        stu_B[Y] += 1
r = 0
for i in range(1, 7):
    r += stu_G[i]//K
    r += stu_B[i]//K
    if stu_G[i] % K:
        r += 1
    if stu_B[i] % K:
        r += 1
print(r)





