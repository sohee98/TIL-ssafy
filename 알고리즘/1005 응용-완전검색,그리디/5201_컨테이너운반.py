import sys
sys.stdin = open(f'5201sample_input.txt', "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    weight.sort(reverse=True)
    truck.sort(reverse=True)
    sumV = 0
    j = 0
    for i in range(M):      # 트럭 수 만큼
        while j < N and truck[i] < weight[j]:
            j += 1
        if j > N-1:
            break
        if truck[i] >= weight[j]:
            sumV += weight[j]
            j += 1
    print('#{} {}'.format(tc,sumV))