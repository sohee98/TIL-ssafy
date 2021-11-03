import sys
sys.stdin = open(f'5356ample_input.txt', "r")

def mymax(lst):
    maxV = 0
    for l in range(len(lst)):
        if len(lst[l]) > maxV:
            maxV = len(lst[l])
    return maxV

T = int(input())
for t in range(1, T+1):
    word_list = []
    for i in range(5):
        word = input()
        word_list.append([word[w] for w in range(len(word))])

    maxL = mymax(word_list)
    result_word = [[] for _ in range(maxL)]
    for i in range(maxL):
        for j in range(5):
            if i < len(word_list[j]):
                result_word[i].append(word_list[j][i])

    print('#{}'.format(t), end=' ')
    for a in range(len(result_word)):
        for b in range(len(result_word[a])):
            print(result_word[a][b], end='')
    print()