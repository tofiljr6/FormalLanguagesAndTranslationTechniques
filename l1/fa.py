def FAMatcher(T, delta, m, s):
    """
    T - text represents as array [0...n]
    delta - transition function
    m - number of states 
    """
    n = len(T)
    q = 0
    for i in range(n):
        q = delta[q][s.get(T[i])]
        if q == m:
            print("Pattern occurs with shift", i - m + 1)


# computing the transition function
def computeTransitionFunction(P, S):
    """
    P - pattern
    S - dictinary
    """
    # create the transition function and fill deflaut value 0
    delta = [[0 for i in range(len(S))] for j in range(len(P)+1)]

    m = len(P)
    for q in range(m+1):
        for a in S:
            k = min(m+1, q+2) - 1
            while not (P[0:q]+a).endswith(P[:k]):
                k -= 1
            delta[q][S.get(a)] = k
    return delta

def createDict(t):
    """
    The function creates a dictionary (sigma) of the t (text:input)
    """
    iterator = 0
    dictionary = {}

    for letter in t:
        if letter not in dictionary:
            dictionary.update({letter:iterator})
            iterator += 1

    return dictionary

def stringtoArray(string):
    """
    The function converts input string to array of single character.

    string - input string
    """
    return [string[i] for i in range(len(string))]
