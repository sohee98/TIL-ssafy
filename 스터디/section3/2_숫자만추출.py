import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션3_입출력/2. 숫자만 추출/in{i}.txt', "r")
    string = input().upper()
    num = []

    def divisors(num):
        result = 0
        for i in range(1, num+1):
            if num % i == 0:
                result += 1
        return result

    for n in range(len(string)):
        if 65 <= ord(string[n]) <= 90:
            continue
        else:
            num.append(string[n])

    number = ''.join(num)
    number = int(number)
    print(number)
    print(divisors(number))
    print('-----------------------------------')