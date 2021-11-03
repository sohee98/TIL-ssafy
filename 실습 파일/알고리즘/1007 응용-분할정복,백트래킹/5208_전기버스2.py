import sys
sys.stdin = open(f'5208sample_input.txt', "r")

def solve(k, remain, cnt):
    global minC

    if minC <= cnt:
        return

    if k==lst[0]:
        if minC > cnt:
            minC = cnt
        return

    if remain == 0:     # 못가는 경우
        return

    solve(k+1, lst[k+1], cnt+1)
    solve(k+1, remain-1, cnt)



T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split())) + [0]
    minC = 100
    solve(1, lst[1], 0)
    print('#{} {}'.format(tc, minC))