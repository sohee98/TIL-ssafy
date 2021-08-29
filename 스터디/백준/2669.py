XY = [[0]*101 for _ in range(101)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            XY[y][x] = 1
sumV = 0
for s in XY:
    sumV += sum(s)
print(sumV)
