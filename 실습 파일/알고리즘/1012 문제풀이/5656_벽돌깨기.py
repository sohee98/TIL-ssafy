import sys
sys.stdin = open(f'5656sample_input.txt', "r")
import copy
# copy.deepcopy()

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solve(ARR, k):
    global minV
    if k == N:
        cnt = 0
        for i in range(W):
            for j in range(H):
                if ARR[j][i]:
                    cnt += 1
        if cnt < minV:
            minV = cnt
        return

    for i in range(W):  # 열
        # 백업
        tmp = copy.deepcopy(ARR)
        # 벽돌제거
        for j in range(H):  # 행
            if ARR[j][i]:       # 0이 아니면 = 첫번째 벽돌
                num = ARR[j][i]
                ARR = remove(ARR, j, i, num)
                break
        # 정리작업
        ARR = clean(ARR)
        # 다음 단계
        solve(ARR, k+1)
        # 복구
        ARR = copy.deepcopy(tmp)

# 벽돌 제거
def remove(ARR, j, i, num):
    for n in range(num):  # 벽돌에 적힌 숫자만큼
        for d in range(4):  # 상하좌우
            nj = j + dr[d] * n
            ni = i + dc[d] * n
            if 0 <= nj < H and 0 <= ni < W and ARR[nj][ni]:
                num2 = ARR[nj][ni]
                ARR[nj][ni] = 0
                if num2 > 1:
                    remove(ARR, nj, ni, num2)
    return ARR

# 정리작업
def clean(ARR):
    for i in range(W):
        ST = []         # 남은 벽돌
        for j in range(H):
            if ARR[j][i]:
                ST.append(ARR[j][i])
                ARR[j][i] = 0
        for j in range(H-1, -1, -1):
            if ST:
                ARR[j][i] = ST.pop(-1)
    return ARR


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())         # N번, W:가로, H:세로
    ARR = [list(map(int, input().split())) for _ in range(H)]
    minV = W*H
    solve(ARR, 0)
    print('#{} {}'.format(tc, minV))


