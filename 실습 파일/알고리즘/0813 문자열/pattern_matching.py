# 고지식한 알고리즘
T = 'TTTTAACCAVCEDTTATTTF'
# P = 'TTATTT'

def pattern_B(P):
    lenT = len(T)
    lenP = len(P)

    for idxT in range(lenT - lenP + 1):
        idxP = 0
        while idxP < lenP and P[idxP] == T[idxT+idxP]:
            idxP += 1
        if idxP == lenP:        # 찾음
            return idxT
        else:                   # 못찾음
            idxT += 1
    return -1

print(pattern_B('TTATTT'))
print(pattern_B('TTTA'))
print('======================================')


# 보이어-무어 알고리즘
# def pattern_BMOOR(P):
#     lenT = len(T)
#     lenP = len(P)
#
#     jumpA = [lenP]*128
#     value = 0
#     for i in range(lenP, -1, -1):
#         c = P[i]
#         jumpA[ord(c)] = value
#         value += 1
#
#     idxT = 0
#     while idxT < lenT - lenP:
#         idxP = lenP-1
#         # 역으로 비교
#         while idxP < lenP and P[idxP] == T[idxT+idxP]:
#             idxP += 1
#         if idxP == lenP:        # 찾음
#             return idxT
#         else:                   # 못찾음
#             jumpA
#     return -1

T = 'Prithm Process finished with exit code 0'

def BM(P):
    M = len(P)
    N = len(T)

    SKIP = [M] * 128
    for i in range(M):
        # pos = ord(P[i])
        # SKIP[pos] = M-i-1
        SKIP[ord(P[i])] = M - i - 1

    idxT = 0
    while idxT <= N-M:
        idxP = M-1
        while idxP >= 0 and T[idxT+idxP] == P[idxP]:
            idxP -= 1
        if idxP == -1:      # 찾음
            return idxT
        idxT = idxT + SKIP[ord(T[idxT+M-1])]
    return -1

    # print(SKIP[ord('r')], SKIP[ord('t')], SKIP[ord('m')])

print(BM('rithm'))

