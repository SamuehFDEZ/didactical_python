# accessing string

#index
a = "Hola"
print(a[0])
print(a[1])
print(a[2])
print(a[3])

print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])

# len()
print(len(a))
i = 0
length = len(a)
while i < length:
    print(a[i])
    i += 1

for i in range(length):
    print(a[i])



#slice operator
#string_name(start_index: end_index: steo)

b = "Python"

print(b[0:6:3])
#only prints "ython"
print(b[1::])
# starts in the default value until the 4th character
# by default steps by 1
print(b[:4:])
#prints the entire string
print(b[::])


#operations on string

# addition (+)
# multiplication (*)

c = "Python"
d = " Programming"
e = c + d
print(e)

f = c * 2
print(f)

# Membership test
# allows us to check if a char or string is present in
# the given string using membership operators (in not in)

g = "python"
print("s" not in g)
































