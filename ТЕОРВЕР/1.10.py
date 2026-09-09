from itertools import permutations

O = ['Т', 'Е', 'О', 'Р', 'И', 'Я']
A = list(permutations(O, 3))
TOP = A.count(('Т', 'О', 'Р'))
print(TOP / len(A))

B = list(permutations(O, 6))
TEOP = B.count(('Т','Е','О','Р','И','Я',))
print(TEOP / len(B))
