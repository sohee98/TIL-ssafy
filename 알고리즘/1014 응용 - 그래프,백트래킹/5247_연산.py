import sys
sys.stdin = open(f'5247sample_input.txt', "r")

from collections import deque

# 너비우선 - 재귀
def bfs(Q, k):      # V:숫자 리스트, k:횟수
    global ans
    if M in Q:
        ans = k
        return
    newQ = []
    for s in Q:
        t = [s+1, s-1, s*2, s-10]
        for newV in t:
            if 0 < newV <= 1000000 and not visited[newV]:
                visited[newV] = True
                newQ.append(newV)
    bfs(newQ, k+1)

def solve():
    Q = deque()
    visited = [False] * 1000001
    Q.append((N,0))
    while Q:
        curV, cnt = Q.popleft()
        if curV == M:
            break
        else:
            t = [curV+1, curV-1, curV*2, curV-10]
            for newV in t:
                if 0 < newV <= 1000000 and not visited[newV]:
                    visited[newV] = True
                    Q.append((newV, cnt+1))
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # +1, -1, *2, -10
    # Q = [N]
    # bfs(Q, 0)
    print('#{} {}'.format(tc, solve()))
