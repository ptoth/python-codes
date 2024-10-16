# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Examples:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.
num = 117
name = "Spartan"
print(type(num))
print(type(name))

# String variables can be declared either by using single or double quotes:
noName = "John Doe" # is the same as
noName = 'John Doe'

# Variable names are case-sensitive.
myvariable = 4
myVariable = "Good"
MyVariable = "You"

print(myVariable + " " + str(myvariable) + " " + MyVariable)

# Python allows you to assign values to multiple variables in one line:
# not recommended
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables.
# This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) # will be apple
print(y) # banana
print(z) # charry
