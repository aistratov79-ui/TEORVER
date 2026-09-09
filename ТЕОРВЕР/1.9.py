from itertools import permutations

digits = [4, 4, 4, 5, 5, 6, 6]
res = len(set(permutations(digits)))
print(res)