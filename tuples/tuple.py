# Properties of tuple

# Insertion order is preserved

# Duplicate objects are allowed

# Allows elements of different data type to be stored

# Data in tuple is fixed and cannot be changed

# Index as backbone

# Allows you to differentiate between duplicate objects

# Preserves the insertion order of tuple
#list
a = [1,2,3]
print(type(a))

# tuple
b = (1,2,3)
print(type(b))

# empty tuple
a = ()
print(type(a))
#int if we put only one element
a = (1)
print(type(a))

#tuple with only one element (add a comma)
a = (1,)
print(type(a))

# without parenthesis
a = 1,2,3
print(type(a))

# list to tuple

l = [1,2,3]
print("l:",type(l))
t = tuple(l)
print("t:",type(t))

# nested tuple
nest_tuple = (1,(2,3))
print("nest_tuple:",nest_tuple)

# tuple with mixed datatype

z = (1,"a","b",2)
print("z:",type(z))
print("z:",z)















