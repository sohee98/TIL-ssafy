def find_parent(t):
    parent_list = [t]
    while child_parent[t]:
        parent_list.append(child_parent[t])
        t = child_parent[t]
    return parent_list

def find_child(t, allchild):
    while len(parent_child[t]):
        for i in range(len(parent_child[t])):
            allchild.append(parent_child[t][i])
            find_child(parent_child[t][i], allchild)
        return

T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    lst = list(map(int, input().split()))
    parent_child = [[] for _ in range(V+1)]   # idx:부모, 값:자식
    child_parent = [[] for _ in range(V+1)]   # idx:자식, 값:부모
    for i in range(0, E*2, 2):
        parent_child[lst[i]].append(lst[i+1])
        child_parent[lst[i+1]] = lst[i]
    A_list = find_parent(A)
    B_list = find_parent(B)
    for a in A_list:
        if a in B_list:
            Parent = a      # 가장 가까운 공통조상
            break
    allchild = [Parent]
    find_child(Parent, allchild)
    print('#{} {} {}'.format(tc, Parent, len(allchild)))
