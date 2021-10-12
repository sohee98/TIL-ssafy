import sys
sys.stdin = open(f'4012sample_input.txt', "r")

def pick(k):
    global minV
    if k == N//2:
        A = []  # A가 선택한 식재료 번호
        B = []  # B가 선택한 식재료 번호
        for i in range(N):
            if P[i]:
                A.append(i)
            else:
                B.append(i)
        resA = resB = 0
        for a1 in range(len(A)):
            for a2 in range(a1, len(A)):
                resA += S[A[a1]][A[a2]] + S[A[a2]][A[a1]]
                resB += S[B[a1]][B[a2]] + S[B[a2]][B[a1]]
        res = abs(resA - resB)
        minV = min(minV, res)
        return
    for i in range(N):
        if not P[i]:
            P[i] = 1
            pick(k+1)
            P[i] = 0

def combi(N, M, k, s, res):
    global minV
    if k == M:
        A = list(res)
        B = list(set(num)-set(res))
        resA = resB = 0
        for a1 in range(len(A)):
            for a2 in range(a1, len(A)):
                resA += S[A[a1]][A[a2]] + S[A[a2]][A[a1]]
                resB += S[B[a1]][B[a2]] + S[B[a2]][B[a1]]
        res = abs(resA - resB)
        minV = min(minV, res)
        return
    for i in range(s, N-M+k+1):
        res[k] = i
        combi(N, M, k+1, i+1, res)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    minV = 40000
    # P = [0]*N   # A가 선택한 식재료 = 1
    # pick(0)
    M = N//2
    res = [-1]*M
    num = list(range(N))
    combi(N, M, 0, 0, res)
    print('#{} {}'.format(tc,minV))
