import sys
sys.stdin = open(f'5207sample_input.txt', "r")

def find(lst, b):
    global isLeft, isRight, s
    if len(lst) <= 0:
        return
    l = 0
    r = len(lst)-1
    m = (l+r)//2
    if lst[m] > b and isRight:          # 왼쪽구간 선택
        isLeft = True
        isRight = False
        find(lst[:m], b)
    elif lst[m] < b and isLeft:        # 오른쪽 구간 선택
        isRight = True
        isLeft = False
        find(lst[m+1:], b)
    elif lst[m] == b:
        s = True
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = 0
    for b in range(M):
        s = False
        isLeft = True
        isRight = True
        find(A, B[b])
        if s:
            res += 1
    print('#{} {}' .format(tc, res))