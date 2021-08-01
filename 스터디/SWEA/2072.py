T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
	num = list(map(int, input().split()))
	sumV = 0
	for n in num:
   		if n % 2 != 0 : sumV = sumV + n
	print(f'#{i} {sumV}')