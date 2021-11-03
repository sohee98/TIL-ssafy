import sys
sys.stdin = open(f'5207sample_input.txt', "r")

def find(lst, b):
    global isLR
    if len(lst) <= 1:
        return 0
    m = (len(lst)-1)//2
    if lst[m] == b:
        return 1
    elif lst[m] > b:    # 왼쪽구간 선택
        if isLR == 'L':
            return 0
        isLR = 'L'
        return find(lst[:m], b)
    else:               # 오른쪽 구간 선택
        if isLR == 'R':
            return 0
        isLR = 'R'
        return find(lst[m+1:], b)
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = 0
    for b in range(M):
        isLR = ''
        s = find(A, B[b])
        if s:
            res += 1
    print('#{} {}' .format(tc, res))