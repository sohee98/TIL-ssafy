import sys
sys.stdin = open(f'4880sample_input.txt', "r")
# 1가위 2바위 3보
def rock(i, j):
    a = card[i]
    b = card[j]
    if a == 1:
        if b == 2:
            return j
        else:
            return i
    if a == 2:
        if b == 3:
            return j
        else:
            return i
    if a == 3:
        if b == 1:
            return j
        else:
            return i

def game(i, j):         # i, j 안의 영역을 반으로 나누어 이기는 번호(위치)를 반환.
    win1 = i
    win2 = j
    if j-i > 1:
        win1 = game(i, (i+j)//2)
        win2 = game((i+j)//2+1, j)
    winner = rock(win1, win2)
    return winner

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    card.insert(0,0)
    print('#{} {}'.format(tc,game(1, N)))


