N, M = map(int, input().split())        # N세로, M가로
r, c, d = map(int, input().split())     # r,c 청소기 / d:0북,1동,2남,3서
arr = [list(map(int, input().split())) for _ in range(N)]
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
res = 0
while True:
    if arr[r][c] == 0:
        arr[r][c] = 2       # 현재 위치 청소
        res += 1
    # 북0->서3, 동1->북0, 남2->동1, 서3->남2
    nr = r + dr[(d+3)%4]    # 왼쪽 방향 공간 (nr,nc)
    nc = c + dc[(d+3)%4]
    if arr[nr][nc] == 0:    # 청소하지 않았다면
        d = (d+3) % 4       # 회전
        r, c = nr, nc       # 한칸 전진
        continue
    if arr[r-1][c] and arr[r][c+1] and arr[r+1][c] and arr[r][c-1]:
        nr = r + dr[(d + 2) % 4]  # 뒤쪽 방향 공간 (nr,nc)
        nc = c + dc[(d + 2) % 4]
        if arr[nr][nc] == 1:
            break
        else:
            r, c = nr, nc
            continue
    if arr[nr][nc]:         # 청소했다면
        d = (d+3) % 4  # 회전
        continue
print(res)