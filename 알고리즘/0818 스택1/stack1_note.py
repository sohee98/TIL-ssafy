## stack 구현
def push(item):
    s.append(item)

def pop():
    if len(s)==0:
        return -1
    return s.pop(-1)

# s = []
# push(1)
# push(2)
# push(3)
# push(4)
# push(5)
# print(pop())    # result1 = pop()
# print(pop())
# print(pop())
# print(pop())
# print(pop())


## 괄호검사
def check(test):
    ST = []
    for c in test:
        if c == '(':
            ST.append(c)
        if c == ')':
            if len(ST) == 0:
                return False
            ST.pop(-1)
    if len(ST) == 0:
        return True
    else:
        return False

# s1 = '()()((()))'
# s2 = '((()((((()()((()())((())))))'
# s3 = '())'
# print(check(s1))
# print(check(s2))
# print(check(s3))


## Function call
# 디버그 실행해서 확인. F7
def F_2():
    print('2_1')   #5
    print('2_2')   #6
    return         #7

def F_1():
    print('1_1')    #3     #13
    F_2()           #4, #8
    print('1_2')    #9
    return          #10

# print('1')       #1
# F_1()            #2
# print('2')       #11
# F_1()            #12
# print('3')


## 재귀함수
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(4))











