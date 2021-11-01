def find_parent(t):
    parent_list = [t]
    while tree[t]:
        parent_list.append(tree[t])
        t = tree[t]
    return parent_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        parent, child = map(int, input().split())
        tree[child] = parent
    A, B = map(int, input().split())
    A_list = find_parent(A)
    B_list = find_parent(B)
    for a in A_list:
        if a in B_list:
            print(a)
            break