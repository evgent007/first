a = {1,2}
b = {2,3}
c = a & b
d = a|b
e = a^b
print(c,d,e,sep = '\n')
print(a.union(b))
print(a)
c1 = a.intersection(b)
print(c1)
ab = a.difference(b)
print(ab)
e1 = a.symmetric_difference(b)
print(e1)
a.difference_update(b)
print(a)
