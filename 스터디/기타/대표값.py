import sys
for i in range(1,6):
    sys.stdin=open(f'./섹션2_입출력/4. 대표값/in{i}.txt', "r")
    n = int(input())
    score = list(map(int, input().split()))
    avg = round(sum(score)/len(score))
    diff = []
    for i in range(n):
        diff.append(abs(score[i]-avg))
    stu = []
    for j in range(n):
        if diff[j]==min(diff):
            stu.append(j+1)
    if len(stu) == 1:
        print(avg, stu[0])
    elif len(stu) == 2:
        if score[stu[0]-1] >= score[stu[1]-1]:
            print(avg, stu[0])
        else:
            print(avg, stu[1])
    else:
        print(avg, stu[0])



