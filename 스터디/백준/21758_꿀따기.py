# 아직 못품
N = int(input())
lst = list(map(int, input().split()))

def find(a, h):      # 벌 위치, 꿀 위치
    r = 0
    if a<h:     # 벌, 꿀      3, 6
        for id in range(1, h-a+1):    # 4
            if not v[a+id]:
                r += lst[a+id]
    elif a>h:   # 꿀, 벌      6, 2
        for id in range(a-h):
            if not v[h+id]:
                r += lst[h+id]
    return r

v = [0]*N       # 벌이 있으면 1
maxV = 0
for i in range(N):
    v[i] = 1
    for j in range(N):
        if not v[j]:
            v[j] = 1
        for h in range(N):
            if not v[h]:
                res = find(i, h)
                res += find(j, h)
                print(res)
                if res > maxV:
                    maxV = res
print(maxV)