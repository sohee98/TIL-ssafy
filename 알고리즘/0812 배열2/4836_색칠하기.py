import sys
sys.stdin = open(f'4836sample_input.txt', "r")
T = int(input())
for t in range(1, T+1):
    N = int(input())
    color_list = []
    for i in range(N):
        color_list += [list(map(int, input().split()))]
    red = []
    blue = []
    for c in range(N):
        color = color_list[c]
        if color[4] == 1:
            for x in range(color[0], color[2]+1):
                for y in range(color[1], color[3]+1):
                    red.append((x, y))
        if color[4] == 2:
            for x in range(color[0], color[2] + 1):
                for y in range(color[1], color[3] + 1):
                    blue.append((x, y))
    purple = 0
    for i in range(len(red)):
        if red[i] in blue:
            purple += 1
    print('#{} {}' .format(t, purple))