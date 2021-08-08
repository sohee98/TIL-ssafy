import sys
for i in range(1,6):
    sys.stdin=open(f'./섹션2_입출력/3. k번째 큰 수/in{i}.txt', "r")
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    numlst = []
    for a in range(n):
        for b in range(a+1,n):
            for c in range(b+1,n):
                sumV = num[a]+num[b]+num[c]
                if sumV not in numlst:
                    numlst.append(sumV)
    numlst.sort(reverse=True)
    print(numlst[k-1])



