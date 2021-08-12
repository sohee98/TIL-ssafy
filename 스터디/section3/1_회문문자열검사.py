import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션3_입출력/1. 회문 문자열 검사/in{i}.txt', "r")
    N = int(input())
    word_list = []
    for n in range(1, N+1):
        word = input().lower()
        word_len = len(word)
        result = 'YES'
        for l in range(len(word)//2):
            if word[l] != word[word_len-l-1]:
                result = 'NO'
                break
        print('#{} {}' .format(n, result))
    print('-----------------------------------')


