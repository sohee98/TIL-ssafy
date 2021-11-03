import sys
sys.stdin = open(f'5174sample_input.txt', "r")

def find(n):
    global cnt
    if node[n][0]:
        cnt += 1
        find(node[n][0])
    if node[n][1]:
        cnt += 1
        find(node[n][1])
    if node[n][0] == 0 or node[n][1] == 0:
        return cnt

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    node = [[0]*2 for _ in range(E + 2)]
    for i in range(0, 2*E, 2):
        if node[lst[i]][0] == 0:
            node[lst[i]][0] = lst[i+1]
        else:
            node[lst[i]][1] = lst[i+1]
    cnt = 1
    find(N)
    print('#{} {}'.format(t,cnt))

