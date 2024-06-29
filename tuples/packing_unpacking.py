# Packing variables into the tuple
a = 10
b = 11
c = 12
d = 13
t = a,b,c,d
print(t)
print(type(t))

# Unpacking
w, x, y, z = t

print(w)
print(x)
print(y)
print(z)

# too many values to unpack
# as t has 4 values cannot accept only 2 values
w, x = t

# list vs tuple

# list -> []
# tuple -> ()

# list is mutable, updating elements
# tuple is immutable we cannot update the elements,
# though we can access using index

# list is used where content is not fixed and needs
# to be constantly updated

# tuple is used where in content is not required to be updated and is
# fixed









