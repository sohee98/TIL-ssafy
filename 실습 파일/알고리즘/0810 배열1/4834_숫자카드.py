import sys
sys.stdin = open("4834sample_input.txt", "r")

def myMax(counts):
    max_count = 0
    for c in range(len(counts)):
        if counts[c] >= max_count:
            max_count = counts[c]
            max_card = c            # 높은 장수를 가지고있는 카드의 숫자 = count의 인덱스
    return max_card, max_count

T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))

    counts = [0]*10                  # 0~9카드 장수 세기 [0,0,0,1...] => 각 자릿수에 각 카드 장수
    for n in range(N):
        counts[card[n]] += 1
    max_card, max_count = myMax(counts)  # 가장 높은 장수와 그 숫자 찾기

    print('#{} {} {}'.format(t, max_card, max_count))



