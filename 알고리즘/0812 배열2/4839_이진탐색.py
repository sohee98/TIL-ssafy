import sys
sys.stdin = open(f'4839sample_input.txt', "r")

def mycount(page, p):
    left = 1
    right = p
    cnt = 0
    while left <= right:
        c = (left + right)//2
        cnt += 1
        if page < c:
            right = c
        elif page > c:
            left = c
        else:
            break
    return cnt

T = int(input())
for t in range(1, T+1):
    P, A, B = map(int, input().split())
    if mycount(A, P) > mycount(B, P):
        print('#{} B' .format(t))
    elif mycount(A, P) < mycount(B, P):
        print('#{} A' .format(t))
    else:
        print('#{} 0'.format(t))
