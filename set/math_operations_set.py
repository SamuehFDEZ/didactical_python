# union()
a = {1,2,3,4,5,6,7,8,9,10}
b = {11,12,13,14,15,16,17,18,19,20}
c = a.union(b)
z = a | b
print(c)

# intersection() set of common elements in the set

d = {1,2,3,4,5,6,7,8,9,10}
e = {11,2,13,14,15,16,17,18,19,20}
f = d.intersection(e)
f = d & e

# {2}
print(f)

# difference()
# {1, 3, 4, 5, 6, 7, 8, 9, 10}
print(d.difference(e))
print(d - e)

# symetric_difference() excludes the common elements
# {1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20}
print(d.symmetric_difference(e))
print(d ^ e)


