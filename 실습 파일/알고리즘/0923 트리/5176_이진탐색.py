import sys
sys.stdin = open(f'5176sample_input.txt', "r")

def in_order(root):
    global value
    if root <= N:
        in_order(root*2)
        tree[root] = value
        value += 1
        in_order(root*2+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    value = 1
    in_order(1)
    print('#{} {} {}' .format(t, tree[1], tree[N//2]))
