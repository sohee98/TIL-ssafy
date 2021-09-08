
def mySum(lst):
    sumV = 0
    for i in range(len(lst)):
        sumV += lst[i]
    return sumV
def diff(lst):
    global cnt
    for i in range(len(lst)):
        if lst[i] != lst[i+1]:
            cnt += 1
            return diff(lst[1:])
    return cnt

M, N = map(int, input().split())    # M-세로 * N-가로
B = [input() for _ in range(M)]

c_list = []
cnt = 0
for i in range(M):
    c = diff(B[i])
    print(c)

# minS = 32               # 칠해야하는 정사각형 최대값 = 4*8
# for n in range(M-6):
#     s = mySum(r_list[n:n + 8])
#     if minS > s:
#         minS = s        # 칠해야하는 정사각형 합 최소값 구하기
# print(minS)


