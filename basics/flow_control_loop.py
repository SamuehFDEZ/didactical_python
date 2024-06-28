# if condition:
#   code to be executed

a = 10
b = 5

if a > b:
    print("a is greater than b")
elif a <= b:
    print("a is less than b")
else:
    print("a is equal to b")


# for loop
# sequence = a list of item
# for x in sequence
    # body

a = [1,2,3,4,5,6]

for i in a:
    print(i)
# with string
b = "Hello World"
for i in b:
    print(i)

# range()
for i in range(0,10, 2):
    print(i)

# For with else
for x in a:
    print(x)
else:
    print("no change")


# while loop

# while condition:
#   body

a = 1

while a <= 10:
    print(a)
    a += 1

b = 1
# while loop with else
while b > 10:
    print(b)
    b += 1
else:
    print("no change")

# break statement

num = 5
while num > 5:
    print(num)
    num -= 1
    if num == 2:
        break
    print("Last statement")
print("Outside while")

z = [1,2,3,4,5,6]
for i in z:
    print(i)
    if i == 3:
        break
    print("Last statement")
print("Outside for")

# continue statement

a = 5
while a:
    print(a)
    a = a - 1
    if a == 2:
        continue
    print("Remaining statements")

# pass statement
# used to define an empty block
# pass to have an empty value, for example:

# while a: X
# while a:
    #pass CORRECT


a = 5
while a:
    print(a)
    a = a - 1
    if a == 2:
        pass
    print("Remaining statements")






