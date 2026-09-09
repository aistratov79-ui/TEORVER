from math import comb

m = comb(9, 2) * comb(8, 7)
n = comb(36,7)
print(m/n)
m2 = comb(9,7) * 4**7
n2 = comb(36,7)
print(m2/n2)
m3 = comb(9,3) * (6 * comb(4,4) * comb(4,2) * comb(4,1) + 3 * comb(4,3) * comb(4,3) * comb(4,1) + 3 * comb(4,3) * comb(4,2) * comb(4,2))
n3 = comb(36,7)
print(m3/n3)