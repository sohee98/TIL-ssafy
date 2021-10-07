N = int(input())
romeN = [1, 5, 10, 50]

sum_list = []
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            p = N-i-j-k
            sumV = i + j*5 + k*10 + p*50
            if sumV not in sum_list:
                sum_list.append(sumV)

print(len(sum_list))