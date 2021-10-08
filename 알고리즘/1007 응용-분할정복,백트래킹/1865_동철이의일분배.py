import sys
sys.stdin = open(f'1865input.txt', "r")

def solve(k=0, res=1):
    global maxV
    if k == N:
        res *= 100
        # print(res)
        if res > maxV:
            maxV = res
        return
    if res*100 <= maxV:
        return
    for i in range(N):
        if not v[i] and arr[k][i]:     # k번째 줄, 일이 아직 안됬고 성공확률 0이 아닐때
            v[i] = 1
            # print(arr[k][i], v)
            solve(k+1, res*arr[k][i]/100)
            v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N       # k번째 일 했는지 여부
    lst = [1]*N
    maxV = 0
    solve(0, 1)
    print("#{} {:.6f}".format(tc, maxV))


'''
def solve(k=0):
    global maxV
    if k == N:
        res = 100
        for j in range(len(lst)):
            res *= lst[j]
        if res > maxV:
            maxV = res
        return
    for i in range(N):
        if not v[i] and arr[k][i] != 0:     # k번째 줄, 일이 아직 안됬고 성공확률 0이 아닐때
            lst[k] = arr[k][i]/100
            v[i] = 1
            solve(k + 1)
            v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N       # k번째 일 했는지 여부
    maxV = 0
    solve(0)
    print("#{} {:.6f}".format(tc, maxV))
'''