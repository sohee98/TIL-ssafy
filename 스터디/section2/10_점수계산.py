import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션2_입출력/10. 점수 계산/in{i}.txt', "r")
    N = int(input())
    ans = list(map(int, input().split()))
    score = ans[0]
    con = ans[0]
    score_list = []
    score_list.insert(0, ans[0])
    for i in range(1, N):
        if ans[i] == 1:
            con += 1
            if ans[i-1] == 1:
                score = con
                score_list.append(score)
            else:
                score = 1
                score_list.append(score)
        else:
            score = con = 0
            score_list.append(score)
    print(sum(score_list))
    print(score_list)


