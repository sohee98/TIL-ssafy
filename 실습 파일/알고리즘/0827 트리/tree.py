# 순회
def pre_order(n):
    if n:                       # 유효한 정점이면
        print(n)
        pre_order(left[n])      # n의 왼쪽자식으로 이동
        pre_order(right[n])
def in_order(n):
    global cnt
    if n:                       # 유효한 정점이면
        in_order(left[n])      # n의 왼쪽자식으로 이동
        cnt += 1   # 정점의 개수  # print(n)
        in_order(right[n])
def post_order(n):
    if n:                       # 유효한 정점이면
        post_order(left[n])      # n의 왼쪽자식으로 이동
        post_order(right[n])
        print(n)
'''
6
2 1 1 3 2 4 3 5 3 6
'''
V = int(input())
edge = list(map(int, input().split()))
E = V-1     # V개의 정점이 있는 트리의 간선 수
left = [0]*(V+1)    # 부모를 인덱스로 자식번호 저장
right = [0]*(V+1)
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:    # p의 왼쪽자식이 없으면
        left[p] = c
    else:               # 왼쪽자식이 있으면 오른쪽자식으로 저장
        right[p] = c

# cnt = 0
# pre_order(1)
# print(cnt)      # 3을 루트로하는 서브트리의 정점 개수
# print(cnt-1)    # 3의 자손의 수

# 조상 찾기
'''
6
1 2 1 3 2 4 3 5 3 6
'''
V = int(input())
edge = list(map(int, input().split()))
E = V-1     # V개의 정점이 있는 트리의 간선 수
left = [0]*(V+1)    # 부모를 인덱스로 자식번호 저장
right = [0]*(V+1)
par = [0]*(V+1)     # 자식을 인덱스로 부모번호 저장
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:  # p의 왼쪽자식이 없으면
        left[p] = c
    else:           # 왼쪽자식이 있으면 오른쪽자식으로 저장
        right[p] = c
    par[c] = p      # [0, 0, 1, 1, 2, 3, 3] -> 2의부모=1, 3의부모=1 ...

# c = 6       # 6의 조상찾기
# while par[c]:   # 부모가 있으면
#     print(par[c])   # 3 1
#     c = par[c]

# 부모가 없으면 root
root = 1
while par[root]:    # root로 추정한 정점이 부모가 있으면
    root += 1
print(root)


############
# def pre_order2(root):
#     print(root, tree[root])
#     if root*2 <= N:
#         pre_order2(root*2)
#     if root*2 + 1 <= N:
#         pre_order2(root*2+1)
# N = 10
# tree = [i*100 for i in range(N+1)]
# pre_order2(1)

##practice
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
"""
N = 13
inpst = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, inpst.split()))
tree = [[0] * 2 for _ in range(N + 1)]
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    # 조건에따라 선택적으로 입력되도록
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c

def pre_order(n):
    print(n)
    if tree[n][0]:
        pre_order(tree[n][0])
        if tree[n][1]:
            pre_order(tree[n][1])
pre_order(1)
"""









