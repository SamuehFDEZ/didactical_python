# Properties

# Stored as key value pairs
# Duplicate keys are not allowed but duplicate values are allowed
# Mutable
#
a = {}
print(a, type(a))

a = {
     1:"Python",
     2:"Javascript",
     3:"Ruby",
     4:"Java"
}
print(a)

# using dict()
b = dict()
print(b)

c = dict({
     1:"Python",
     2:"Javascript",
     3:"Ruby",
     4:"Java"
})

print(c)

# accessing elements using []
# if a key does not exit throws an error
d = dict({
     0:"C",
     1:"Python",
     2:"Javascript",
     3:"Ruby",
     4:"Java"
})

print(d[0])

# accessing elements using get()
# if a key does not exit throws None
value_d = d.get(5)
print(value_d)

# updating elements

e = dict({
     0:"C",
     1:"Python",
     2:"Javascript",
     3:"Ruby",
     4:"Java"
})
e[1] = "C++"
print(e)

# if we put as parameter an index does not exist
# it creates the index with its respective value
# puts it in the index 6 without a 5 index
e[6] = "C#"
print(e)

# remove elements

# pop()

x = dict({
     0:"C",
     1:"Python",
     2:"Javascript",
     3:"Ruby",
     4:"Java"
})

x.pop(2)
print(x)
# if we pop up a key does not exist throws error

# popItem pops a random value from the dict
print(x)
x.popitem()
print(x)

# del
# # if we del a key does not exist throws error
del x[0]
print(x)

del x
# deletes the entire dic if we print it throws error
# because it doesn't exist

# clear

#x.clear()
#print(x)

# member ship test

# in not in
# works with the index exclusively
y = dict({
     0:"C",
     1:"Python",
     2:"Javascript",
     3:"Ruby",
     4:"Java"
})

print(2 in y)
print(5 in y)
print(2 not in y)
print(5 not in y)

# iterate through dictionary

v = dict({
     0:"C",
     1:"Python",
     2:"Javascript",
     3:"Ruby",
     4:"Java"
})
# for k, v in v.items():
#     print(k,":", v)

for i in v:
    print(i, v[i])


# important functions with dictionaries

# len() dic length
# get()
# keys() returns all keys in dictionary
# values() returns all values in dictionary
# items() returns key value pairs in dictionary

w = dict({
     0:"C",
     1:"Python",
     2:"Javascript",
     3:"Ruby",
     4:"Java"
})

print(len(w)) # 5
print(w.get(5)) # None
print(w.get(3)) # Ruby
print(w.keys()) # dict_keys([0, 1, 2, 3, 4])
print(w.keys()) # dict_keys([0, 1, 2, 3, 4])
# keys() & values() & items() cannot have arguments
print(w.values()) # dict_values(['C', 'Python', 'Javascript', 'Ruby', 'Java'])
print(w.items()) # dict_items([(0, 'C'), (1, 'Python'), (2, 'Javascript'), (3, 'Ruby'), (4, 'Java')])














