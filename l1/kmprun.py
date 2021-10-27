from kmp import *
import sys

txtname = sys.argv[1]
pattern = sys.argv[2]

T = []
file = open(txtname)
for line in file:
    for l in line:
        T.append(l)

KMPMatcher(T, pattern)