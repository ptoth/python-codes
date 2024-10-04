# String functions:
# Note: All string methods returns new values. They do not change the original string.
myTestString = "abc ABC 123 something NOTHING EvErYtHiNg"

myTestString.capitalize() # Converts the first character to upper case
myTestString.casefold() # Converts string into lower case
myTestString.center('#') # Returns a centered string, centered with #
myTestString.count() # Returns the number of times a specified value occurs in a string
myTestString.encode() # Returns an encoded version of the string
myTestString.endswith() # Returns true if the string ends with the specified value
myTestString.expandtabs() # Sets the tab size of the string
myTestString.find() # Searches the string for a specified value and returns the position of where it was found
myTestString.format() # Formats specified values in a string
myTestString.format_map() # Formats specified values in a string
myTestString.index() # Searches the string for a specified value and returns the position of where it was found
myTestString.isalnum() # Returns True if all characters in the string are alphanumeric
myTestString.isalpha() # Returns True if all characters in the string are in the alphabet
myTestString.isdecimal() # Returns True if all characters in the string are decimals
myTestString.isdigit() # Returns True if all characters in the string are digits
myTestString.isidentifier() # Returns True if the string is an identifier
myTestString.islower() # Returns True if all characters in the string are lower case
myTestString.isnumeric() # Returns True if all characters in the string are numeric
myTestString.isprintable() # Returns True if all characters in the string are printable
myTestString.isspace() # Returns True if all characters in the string are whitespaces
myTestString.istitle() # Returns True if the string follows the rules of a title
myTestString.isupper() # Returns True if all characters in the string are upper case
myTestString.join() # Joins the elements of an iterable to the end of the string
myTestString.ljust() # Returns a left justified version of the string
myTestString.lower() # Converts a string into lower case
myTestString.lstrip() # Returns a left trim version of the string
myTestString.maketrans() # Returns a translation table to be used in translations
myTestString.partition() # Returns a tuple where the string is parted into three parts
myTestString.replace() # Returns a string where a specified value is replaced with a specified value
myTestString.rfind('a') # Searches the string for 'a' value, returns the last position
myTestString.rindex() # Searches the string for 'a' value and returns the last position
myTestString.rjust() # Returns a right justified version of the string
myTestString.rpartition() # Returns a tuple where the string is parted into three parts
myTestString.rsplit() # Splits the string at the specified separator, and returns a list
myTestString.rstrip() # Returns a right trim version of the string
myTestString.split() # Splits the string at the specified separator, and returns a list
myTestString.splitlines() # Splits the string at line breaks and returns a list
myTestString.startswith() # Returns true if the string starts with the specified value
myTestString.strip() # Returns a trimmed version of the string
myTestString.swapcase() # Swaps cases, lower case becomes upper case and vice versa
myTestString.title() # Converts the first character of each word to upper case
myTestString.translate() # Returns a translated string
myTestString.upper() # Converts a string into upper case
myTestString.zfill() # Fills the string with a specified number of 0 values at the beginning
