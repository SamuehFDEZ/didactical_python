# Properties
# Duplicates are not allowed
# Insertion order is not preserved
# Set is mutable
# Heterogenous objects are allowed (diff type objects in a set)
# Mathematical operations like union and intersection can be
# performed in set

s = {1,2,3,4,5,6,7,8,9,10}
print(s)

# having duplicate values set does not print the second 2
s1 = {1,2,2,4,5,6,7,8,9,10}
print(s1)

# set of mixed datatypes

s_mix = {1,2,3,4,5,"a","b","c"}
print(s_mix)

# converting list to set
l = [1,2,3,4,5,6,7,8,9,10]
set_l = set(l)
print(set_l)

# set cannot have mutable objects like list, set
# a = {1,2,{11,22,44}}
# TypeError: unhashable type: 'set'
# print(a)
#a = {1,2, [11,22,44]}
# TypeError: unhashable type: 'list'
#print(a)

# empty set
a = {}
print(a)

# empty set with set()

empty_set = set()
print(empty_set)

# modify set
# add()

mod_set = {1,2,3,4,5,6,7,8,9,10}
print(mod_set)
mod_set.add(11)
print(mod_set)
# multiple values not allowed
# mod_set.add(11,11)
# update to fix this
mod_set.update([12, 22, 33])
print(mod_set)

# update with range()
mod_set.update(mod_set, range(10))
print(mod_set)

# copy() creates a copy of an exisitng set

mod_set_copy = mod_set.copy()
print(mod_set_copy)

# removing elements from set

removing_set = {1,2,3,4,5,6,7,8,9,10}

# pop()
print(removing_set.pop())
print(removing_set)

# remove(x)
removing_set.remove(4)
print(removing_set)

# discard(x) doesnt through an error if an element doesnt exist
# compaerd to remove
removing_set.discard(40)
print(removing_set)

# clear()
removing_set.clear()
print(removing_set)


