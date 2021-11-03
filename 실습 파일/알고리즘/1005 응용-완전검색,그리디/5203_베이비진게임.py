import sys
sys.stdin = open(f'5203sample_input.txt', "r")

def babygin(lst):
    for i in range(len(lst)):
        if lst[i] >= 3:
            return True
        if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:
            return True
    return False

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    card1 = [0]*12
    card2 = [0]*12
    res = 0
    for i in range(0, 12, 2):
        card1[lst[i]] += 1
        card2[lst[i+1]] += 1
        p1 = babygin(card1)
        p2 = babygin(card2)
        if p1 and not p2:
            res = 1
            break
        if p2 and not p1:
            res = 2
            break
        if p1 and p2:
            break
    print("#{} {}".format(tc, res))



