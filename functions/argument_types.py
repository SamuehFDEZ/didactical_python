# Required arguments
def print_name(name):
    print("Hello",name)

print_name("Samuel")
# Keyword arguments
def user_info(name, age):
    print("Hello",name, "your age is:", age)

user_info(name="Samuel", age=19)
# why do this
# the benefit is to alter the order
user_info(age=19,name="Samuel")
# Default arguments
def user_info_default(name, age=19):
    print("Hello",name, "your age is:", age)

user_info_default(name="Samuel")
# Variable-length arguments
# * variable lenght argument
def greet(*name):
    for s in name:
        print("Hello", s)

greet("Samuel", "Python")