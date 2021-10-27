def KMPMatcher(T, P):
    n = len(T)
    m = len(P)
    pi = ComputePrefixFunction(P)
    q = 0
    for i in range(0, n):
        while q > 0 and P[q] != T[i]:
            q = pi[q-1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            print("Pattern occurs with shift", i - m + 1)
            q = pi[q-1] + 1


def ComputePrefixFunction(P):
    m = len(P)
    pi = [0 for i in range(m)]
    pi[0] = 0
    k = 0
    for q in range(2, m+1):
        while k > 0 and P[k] != P[q-1]:
            k = pi[k-1]
        if P[k] == P[q-1]:
            k += 1
        pi[q-1] = k
    return pi
