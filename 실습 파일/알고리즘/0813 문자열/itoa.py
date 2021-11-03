# 숫자를 문자열로 변환
def myReverse(lst):
    result = []
    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    return result

def itoa(value):
    t = []
    if value < 0:
        isMinus = True
        value = value * -1
    else:
        isMinus = False

    while value > 0:
        t.append(chr(value % 10 + 0x30))
        value //= 10
    # t.reverse()
    t = myReverse(t)
    if isMinus:
        return '-' + ''.join(t)
    else:
        return ''.join(t)

print(itoa(123), type(itoa(123)))
print(itoa(-123), type(itoa(123)))