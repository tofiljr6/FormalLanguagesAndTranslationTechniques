from fa import *
import sys

txtname = sys.argv[1]
pattern = sys.argv[2]

T = []
file = open(txtname)
for line in file:
    for l in line:
        T.append(l)

S = createDict(T)
d = computeTransitionFunction(pattern, S)
FAMatcher(T, d, len(pattern), S)
