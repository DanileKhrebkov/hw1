from random import randint
n1, n2 = 10, 5
a = [randint(1, 10) for i in range(n1)]
print(*a)
b = [randint(1, 10) for i in range(n2)]
print(*b)
c = a + b
print('1)', *c)
c = list(set(a + b))
print('2)', *c)
c = list(set(a) & set(b))
print('3)', *c)
c = list(set(a) | set(b))
print('4)', *c)
c = [min(a), max(a), min(b), max(b)]
print('5)', *c)

