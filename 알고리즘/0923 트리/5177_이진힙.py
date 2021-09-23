import sys
sys.stdin = open(f'5177sample_input.txt', "r")

def compare(a, b):
    if tree[a] > tree[b]:
        tree[a], tree[b] = tree[b], tree[a]
    if a != 1:
        compare(a//2, a)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0] * (N + 1)
    tree[1] = lst[0]
    for i in range(2, N+1):
        tree[i] = lst[i-1]
        compare(i//2, i)    # 부모, 자식 비교
    s = 0
    while N >= 1:
        N = N//2
        s += tree[N]
    print('#{} {}'.format(t,s))
