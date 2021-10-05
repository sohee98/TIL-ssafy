import sys
sys.stdin = open(f'1240input.txt', "r")

dict = {'0001101':0, '0011001':1, '0010011':2,
        '0111101':3, '0100011':4, '0110001':5,
        '0101111':6, '0111011':7, '0110111':8,
        '0001011':9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = [input() for _ in range(N)]

    # 1. 위에서부터 오른쪽끝지점을 찾는다
    for row in range(N):
        if '1' in num[row]:
            col = num[row][::-1].index('1')
            break

    # 2. 코드의 시작점을 계산한다.
    col = M - col - 56
    # print(row, col)

    # 3. 8개의 숫자를 찾는다.
    code = []
    for i in range(8):
        # print(num[row][col:col+7])
        code.append(dict[num[row][col:col+7]])
        col += 7
    # print(code)

    # code = []
    # for j in range(N):
    #     i = M-1
    #     while i >= 0:       # 뒤에서부터 비교
    #         if num[j][i]=='1':
    #             code.insert(0,dict[num[j][i-6:i+1]])
    #             i -= 7
    #         else:
    #             i -= 1
    #     if code:
    #         break

    # 4. 코드 검증
    sumV = 0
    for i in range(len(code)):
        if i % 2:   # 1, 3, 5, 7
            sumV += code[i]
        else:       # 0, 2, 4, 6
            sumV += 3*code[i]
    if sumV % 10:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, sum(code)))