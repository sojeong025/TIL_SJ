from itertools import permutations
from itertools import combinations
from pprint import pprint

a = range(1, 4)
# 순열
b = list(permutations(a, 2))
for i in b:
    pprint(i)
print()
# 조합
c = list(combinations(a, 2))
for i in c:
    pprint(i)