# List items are ordered, changeable, and allow duplicate values.
myFirstList = ["apple", "banana", "cherry"]
print("Current list items: "+str(myFirstList))
print("Length of the list is: "+str(len(myFirstList)))

# List items are indexed, the first item has index [0], the second item has index [1] etc.
print("The third item in the list is :" + myFirstList[2])

# adding a new item to the end of list: chair
myFirstList.append("chair")
print("Current list items: "+str(myFirstList))
print("Length of the list is: "+str(len(myFirstList)))

# adding another banana to the list
myFirstList.append("banana")
print("Current list items: "+str(myFirstList))
print("Length of the list is: "+str(len(myFirstList)))

#list can contain mixed types of data as well:
#For example: string, numeric, boolean
mySecondList = ["BMW", 42, True]
print("Mixed list's contents: "+str(mySecondList))

# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

"""
Note: The length of the list will change when the number of 
items inserted does not match the number of items replaced.
If you insert less items than you replace, 
the new items will be inserted where you specified, 
and the remaining items will move accordingly:
"""

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Note: As a result of the example above, the list will now contain 4 items.

# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Note: As a result of the examples above, the lists will now contain 4 items.

# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
