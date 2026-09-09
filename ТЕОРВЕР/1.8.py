from math import comb
k = 5
n = 10
A1 = n ** k
A2 = comb(n + k -1, k)
print("различные призы : ", A1)
print("одинаковые призы : ", A2)