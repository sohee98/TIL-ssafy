import sys
sys.stdin = open(f'1231input.txt', "r")
def in_order(n):
    if n:           # 유효한 정점이면
        in_order(left[n])
        print(node[n], end='')
        in_order(right[n])

T = 10
for t in range(1, T+1):
    V = int(input())
    left = [0] * (V + 1)  # 부모를 인덱스로 자식번호 저장
    right = [0] * (V + 1)
    node = [0] * (V + 1)    # 노드 알파펫 저장
    for v in range(V):
        n = list(input().split())
        i = int(n[0])
        node[i] = n[1]
        if len(n) > 2:
            left[i] = int(n[2])
        if len(n) > 3:
            right[i] = int(n[3])

    print('#{}'.format(t), end=' ')
    in_order(1)
    print()

