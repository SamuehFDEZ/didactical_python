a = [1,2,3,4,5,6,7,8,9,10,11]
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# add new elements
# Using index to change the value

a[1] = 100
print(a)
# [1, 100, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Using slicing operator to change value
a[2:3] = [500,200]
print(a)
# [1, 100, 500, 200, 4, 5, 6, 7, 8, 9, 10, 11]

# Using append() function
a.append(1000)
print(a)
# [1, 100, 500, 200, 4, 5, 6, 7, 8, 9, 10, 11, 1000]

# Using extend() function
# append a list to an existing list
a.extend([2,4,10])
print(a)
# [1, 100, 500, 200, 4, 5, 6, 7, 8, 9, 10, 11, 1000, 2, 4, 10]

# Using insert() function
# doesnt replace the value on the specify index
a.insert(2,1)
print(a)
#[1, 100, 1, 500, 200, 4, 5, 6, 7, 8, 9, 10, 11, 1000, 2, 4, 10]

a.append(8)

# delete elements

# Using del()
del a[1]
print(a)
# [1, 1, 500, 200, 4, 5, 6, 7, 8, 9, 10, 11, 1000, 2, 4, 10, 8]

del a[2:4]
print(a)
# [1, 1, 4, 5, 6, 7, 8, 9, 10, 11, 1000, 2, 4, 10, 8]

# Using remove()
# range() not allowed in remove()
a.remove(8)
print(a)
# [1, 1, 4, 5, 6, 7, 9, 10, 11, 1000, 2, 4, 10, 8]

# Using pop()
# without parameter deletes last parameter
a.pop()
print(a)
# [1, 1, 4, 5, 6, 7, 9, 10, 11, 1000, 2, 4, 10]
a.pop(5)
print(a)
# [1, 1, 4, 5, 6, 9, 10, 11, 1000, 2, 4, 10]
# Using clear()
a.clear()
print(a)
# []





















