import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션2_입출력/9. 주사위 게임/in{i}.txt', "r")
    N = int(input())
    dice = []
    for num in range(N):
        dice.append(list(map(int, input().split())))

    award = []
    for n in dice:
        for i in n:
            if n.count(i) == 3:
                award.append(10000 + i*1000)
                break
            elif n.count(i) == 2:
                award.append(1000 + i*100)
                break
        else:
            award.append(max(n)*100)
    print(max(award))


