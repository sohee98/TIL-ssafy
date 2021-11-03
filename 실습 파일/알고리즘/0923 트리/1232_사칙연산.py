# 중위 순회 연산
import sys
sys.stdin = open(f'1232input.txt', "r")

def in_order(n):
    if left[n] and right[n]:
        a = tree[in_order(left[n])]
        b = tree[in_order(right[n])]
        if tree[n] == '+':
            tree[n] = a + b
            return n
        elif tree[n] == '-':
            tree[n] = a - b
            return n
        elif tree[n] == '*':
            tree[n] = a * b
            return n
        elif tree[n] == '/':
            tree[n] = a / b
            return n
    else:
        return n


T = 10
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)  # 부모를 인덱스로 왼쪽 자식번호 저장
    right = [0] * (N+1) # 부모를 인덱스로 오른쪽 자식번호 저장
    for _ in range(N):
        lst = input().split()
        if len(lst) == 2:
            tree[int(lst[0])] = int(lst[1])
        else:
            tree[int(lst[0])] = lst[1]
            left[int(lst[0])] = int(lst[2])
            right[int(lst[0])] = int(lst[3])

    in_order(1)
    print('#{} {}'.format(t, int(tree[1])))
