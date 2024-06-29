# ==, != only these can be used to compare lists

a = [1,2,3,4,5]
b = [1,2,3]
c = [1,2,3]
d = [1,2,3,4,5]

# Number of elements
# Content of elements, Case sensitive
# Order of elements

print("a equals b?", a==b)
print("a equals c?",a==c)
print("a equals d?",a==d)
print("b equals c?",b==c)
print("b equals d?",b==d)
print("c equals d?",c==d)
print("c not equals d?",c!=d)
print("a not equals c?",a!=c)
print("b not equals c?",b!=c)
print("d not equals c?",d!=c)