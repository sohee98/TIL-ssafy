T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())        # N:수강생 수, K:과제를 제출한 사람의 수
    num = list(map(int, input().split()))   # 과제 제출한 사람의 번호들
    lst = list(range(1, N+1))   # 전체 번호
    result = list(set(lst)-set(num))
    print('#{}'.format(tc), end=' ')
    print(*result)
