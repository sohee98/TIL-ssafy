import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션2_입출력/8. 뒤집은 소수/in{i}.txt', "r")
    N = int(input())
    num_lst = list(input().split())

    def reverse(x):
        lst = []
        for i in range(len(x)-1, -1, -1):
            lst.append(x[i])
        return ''.join(lst)
        
    def isPrime(x):
        if  int(x) < 2:
            return False
        for i in range(2, int(x)):
            if int(x) % i == 0:
                return False
        return True

    reverse_list = []
    for i in num_lst:
        reverse_list.append(reverse(i))
    for r in reverse_list:
        if isPrime(r) == True:
            print(int(r), end=' ')
    print()
