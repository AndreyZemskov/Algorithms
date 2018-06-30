def prefix_function(S):
    P = [0] * len(S)
    for i in range(2, len(S)):
        j = P[i - 1]
        while j > 0 and S[j] != S[i]:
            j = P[j - 1]
        if S[j] == S[i]:
            j = j + 1
        P[i] = j
    return P

def kmp(S, t):
    """ Knuth – Morris – Pratt algorithm """
    index = -1
    f = prefix_function(S)
    j = 0
    for i in range(len(t)):
        while j > 0 and S[j] != t[i]:
            j = f[j - 1]
        if S[j] == t[j]:
            j = j + 1
        if j == len(S):
            index = i - len(S) + 1
            break
    return index