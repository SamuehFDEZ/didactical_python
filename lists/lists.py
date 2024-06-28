#properties
# duplicate objects allowed
#insertion order is preserved

# index as backbone

# allows you to diff between duplicate objects
#preserves the insertion order of lists

# creating and accessing elements in list

lista = [1,2,3,4,5]
print(lista)

# split() function

text = "I love World of Warships"
text_split = text.split()
#split works without putting double commas split(" ")
print(text_split)

# using list() function

list_function = list(range(0,20 + 1 ,1))
print(list_function)

# list of numbers

a = [1,2,3,4,5]
print(a)

# list of strings

b = ["python","java","javascript"]
print(b)

# list of mixed datatype

c = [1,"a",3,"b",5]
print(c)

# Nested lists
nest_list = [1, 2, ["a", "b"]]
print(nest_list)
print(nest_list[2][0])


# accessing elements of list
a = [1,2,3,4,5,6,7,8,9,10,11]
print(a[1])

#using slice to access element
# list_name[start : stop : step]
print(a[1:10:1])
print(a[11:-1:-1])




