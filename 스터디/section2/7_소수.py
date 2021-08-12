import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션2_입출력/7. 소수(에라토스테네스 체)/in{i}.txt', "r")
    # n = int(input())
    # # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    # sieve = [True] * n

    # # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    # m = int(n ** 0.5)
    # for i in range(2, m + 1):
    #     if sieve[i] == True:           # i가 소수인 경우
    #         for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
    #             sieve[j] = False

    # # 소수 목록 산출
    # print(len([i for i in range(2, n) if sieve[i] == True]))
#----------------------------
    n=int(input())
    ch=[0]*(n+1)
    cnt=0
    for i in range(2, n+1):
        if ch[i]==0:
            cnt+=1
            for j in range(i, n+1, i):
                ch[j]=1
    print(cnt)


        
