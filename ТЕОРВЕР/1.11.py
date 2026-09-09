from itertools import permutations
letters = ['А','Н','А','Н','А','С']
A = list(permutations(letters))
W = A.count(('А','Н','А','Н','А','С'))
print(W/len(A))