import sys
sys.stdin = open(f'1242sample_input.txt', "r")

PATT = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]

def hexToBinStr(arr):
    arr = arr.replace('0', '0000')
    arr = arr.replace('1', '0001')
    arr = arr.replace('2', '0010')
    arr = arr.replace('3', '0011')
    arr = arr.replace('4', '0100')
    arr = arr.replace('5', '0101')
    arr = arr.replace('6', '0110')
    arr = arr.replace('7', '0111')
    arr = arr.replace('8', '1000')
    arr = arr.replace('9', '1001')
    arr = arr.replace('A', '1010')
    arr = arr.replace('B', '1011')
    arr = arr.replace('C', '1100')
    arr = arr.replace('D', '1101')
    arr = arr.replace('E', '1110')
    arr = arr.replace('F', '1111')
    return arr

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    binS = [input() for _ in range(N)]
    for i in range(N):
        binS[i] = hexToBinStr(binS[i][0:M])
    sumV = 0

    # 1. 위에서부터 오른쪽끝지점을 여러개 찾는다
    for row in range(1, N):
        if binS[row].find('1') < 0:
            continue

        col = M*4 - 1  # 1로 끝나는 끝점
        while col >= 56:
            # 암호코드의 첫줄의 끝1의 위치 확인
            # binR = binS[row][::-1]
            if binS[row][col] == '1' and binS[row-1][col]=='0':     # 값이 1이고 위에 값이 0일때
                res = []
                for i in range(8):
                    cnt1 = cnt2 = cnt3 = 0
                    while binS[row][col] == '1':
                        cnt1 += 1
                        col -= 1
                    while binS[row][col] == '0':
                        cnt2 += 1
                        col -= 1
                    while binS[row][col] == '1':
                        cnt3 += 1
                        col -= 1
                    while col>=0 and binS[row][col] == '0':
                        col -= 1
                    r = min(cnt1, cnt2, cnt3)       # 비율
                    res.insert(0, PATT.index(cnt3*100//r+cnt2*10//r+cnt1//r))
                # print(res)

                oddV = res[0] + res[2] + res[4] + res[6]
                evenV = res[1] + res[3] + res[5] + res[7]
                if (oddV*3 + evenV) % 10 == 0:
                    sumV += sum(res)

            else:
                col -= 1

    print('#{} {}'.format(tc,sumV))






