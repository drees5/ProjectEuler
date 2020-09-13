import operator
from collections import Counter
from functools import reduce
from math import factorial


def npermutations(l):
    num = factorial(len(l))
    mults = Counter(l).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    return num / den

print(npermutations('r'*20 + 'd'*20))