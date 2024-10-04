# Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# The following will return True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# In fact, there are not many values that evaluate to False, except empty values, 
# such as (), [], {}, "", the number 0, and the value None. 
# And of course the value False evaluates to False.

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Print the answer of a function:
def myFunction() :
    return True

print(myFunction())

# Print "YES!" if the function returns True, otherwise print "NO!":
def yesOrNoFunction() :
    return True

if yesOrNoFunction():
    print("YES!")
else:
    print("NO!")

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))
