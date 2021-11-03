def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

# for i in range(-5, 6):
    # print("%3d = " % i, end='')
    # Bbit_print(i)

# change endian
def ce(n):
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
    return p
x = 0x01020304
p = ce(x)
# print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))

# 10진수의 값을 2진수로 출력하기
# 10 => 00001010
def dectobinstr(num):
    res = ''
    for j in range(7, -1, -1):
        if num & (1<<7):
            res += '1'
        else:
            res += '0'
    return res
# print(dectobinstr(10))


######### 연습문제1
# lst = '0000000111100000011000000111100110000110000111100111100111111001100111'
# for i in range(0, len(lst), 7):
#     l = lst[i:i+7]
#     num = int('0b'+l, 2)
#     print(num, end=', ')
# print()

# 2진수를 10진수로
def binstrtodec(binstr):
    binstr = list(map(int, binstr))
    res = 0
    for i in range(len(binstr)):
        res = res*2 + binstr[i]
    return res

# for pos in range(0, len(lst), 7):
#     org = lst[pos:pos+7]
    # print(binstrtodec(org))


######### 연습문제2
# lst = '01D06079861D79F99F'
# n10 = []
# n2 = ''
# for i in range(len(lst)):
#     n10.append(int('0x'+lst[i], 16))
#     n2 += format(n10[i], '04b')
# for i in range(0, len(n2), 7):
#     l = n2[i:i+7]
#     num = int('0b'+l, 2)
#     print(num, end=', ')
# print()

# 16진수를 2진수로
def hexToBinStr(hexV):
    # 1. 16진수를 10진수로 바꾼다.
    if hexV.isdigit():
        numV = int(hexV)
    else:
        numV = ord(hexV) - ord('A') + 10
    # 2. 10진수의 값을 2진수로 바꾼다. (dectobinstr())
    tmp_res = ''
    for j in range(3, -1, -1):
        if numV & 1<<j:
            tmp_res += '1'
        else:
            tmp_res += '0'
    return tmp_res

def hexToBinStr2(hexV):
    dict = {'0':'0000', '1':'0001', '2':'0010',
            '3':'0011', '4':'0100', '5':'0101',
            '6':'0110', '7':'0111', '8':'1000',
            '9':'1001', 'A':'1010', 'B':'1011',
            'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    return dict[hexV]

lst = '01D06079861D79F99F'
lst = '0F97A3'
res = ''
for i in range(0, len(lst)):
    res += hexToBinStr(lst[i])

for pos in range(0, len(res), 7):
    org = res[pos:pos+7]
    # print(binstrtodec(org))


########### 연습문제3 - 오른쪽부터
lst = '0DEC'
res = ''
for i in range(len(lst)):
    res += hexToBinStr(lst[i])

patt = ['001101', '010011', '111011', '110001', '100011',
        '110111', '001011', '111101', '011001', '101111']
pos = 0
while pos<len(res):
    if res[pos:pos+6] in patt:
        print(patt.index(res[pos:pos+6]))
        pos += 6
    else:
        pos += 1







