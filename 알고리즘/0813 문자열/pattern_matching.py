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


# 보이어-무어 알고리즘
def pattern_BMOOR(P):
    lenT = len(T)
    lenP = len(P)

    jumpA = [lenP]*128
    value = 0
    for i in range(lenP, -1, -1):
        c = P[i]
        jumpA[ord(c)] = value
        value += 1

    idxT = 0
    while idxT < lenT - lenP:
        idxP = lenP-1
        # 역으로 비교
        while idxP < lenP and P[idxP] == T[idxT+idxP]:
            idxP += 1
        if idxP == lenP:        # 찾음
            return idxT
        else:                   # 못찾음
            jumpA
    return -1


