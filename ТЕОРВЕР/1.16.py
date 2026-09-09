from itertools import permutations
ppl = ['Ж','Ж','Ж','Ж','Ж','М','М','М','М','М']
A = list(permutations(ppl))
cher = A.count(('Ж','М','Ж','М','Ж','М','Ж','М','Ж','М'))
print(cher/len(A) * 2)
from math import factorial
print((factorial(4)*factorial(5))/factorial(9))
print((factorial(5)*2**5)/factorial(10))