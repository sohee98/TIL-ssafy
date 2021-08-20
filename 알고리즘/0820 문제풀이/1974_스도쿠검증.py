import sys
sys.stdin = open(f'1974input.txt', "r")

def Sdoku(lst):
    newN = []
    for i in range(9):
        if lst[i] not in newN and 0<lst[i]<=9:
            newN.append(lst[i])
        else:
            return 0
    return 1

T = int(input())
for t in range(1, T+1):
    S = []
    for i in range(9):
        S.append([n for n in map(int, input().split())])    # 가로 리스트

    S2 = [[S[j][i] for j in range(9)] for i in range(9)]    # 세로 리스트
    S3 = []                                                 # 사각형 리스트
    for i in range(9):
        for j in range(9):
            if i%3==0 and j%3==0:
                S3.append([S[a][b] for a in range(i, i+3) for b in range(j, j+3)])
    result = 1
    for i in range(9):
        if Sdoku(S[i]) == 0 or Sdoku(S2[i]) == 0 or Sdoku(S3[i]) == 0:
            result = 0
    print('#{} {}'.format(t, result))
