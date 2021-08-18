import sys
for t in range(1, 6):
    sys.stdin = open(f'./섹션3_입출력/4. 두 리스트 합치기/in{t}.txt', "r")
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))
    new_list = []
    i = 0
    j = 0
    while i < N and j < M:
        if N_list[i] >= M_list[j]:
            new_list.append(M_list[j])
            j += 1
        else:
            new_list.append(N_list[i])
            i += 1
    if i == N:
        new_list += M_list[j:]
    elif j == M:
        new_list += N_list[i:]

    result = []
    for n in range(len(new_list)):
        result.append(str(new_list[n]))
    print('#{} {}'.format(t, ' '.join(result)))
