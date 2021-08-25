# 순열 - 재귀적 알고리즘
def f(i, N):
    if i == N:      # 순열 완성
        print(P)
    else:           # i번 원소값 결정
        for j in range(i, N):     # 자신부터 오른쪽 원소와 교환
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]
P = [1, 2, 3]
f(0, len(P))


def f(i, N, r):
    if i == r:      # 순열 완성
        print(P[0:r])
    else:           # i번 원소값 결정
        for j in range(i, N):     # 자신부터 오른쪽 원소와 교환
            P[i], P[j] = P[j], P[i]
            f(i+1, N, r)
            P[i], P[j] = P[j], P[i]

# P = [1, 2, 3, 4, 5]     # 숫자는 5개지만
# f(0, len(P), 3)         # 앞부분 3개만 출력







