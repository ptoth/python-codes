# open file
myFile = open("14_test.txt", "r")
# read one line
print(myFile.readline())
# close file
myFile.close()

# open file
myFile = open("14_test.txt", "r")
# sweep through line
for line in myFile:
    print(line)
# close file
myFile.close()

myFirstWrittenFile = open("result.txt", "w", encoding="UTF8")
myFirstWrittenFile.write("This should be the first line\n")
myFirstWrittenFile.close()

myFirstWrittenFile = open("result.txt", "a", encoding="UTF8")
myFirstWrittenFile.write("This should be the appended line")
myFirstWrittenFile.close()

