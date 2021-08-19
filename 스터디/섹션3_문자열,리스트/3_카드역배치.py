import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션3_입출력/3. 카드 역배치/in{i}.txt', "r")
    for t in range(10):
        a, b = map(int, input().split())
        card = []
        for i in range(1, 21):
            card.append(i)

