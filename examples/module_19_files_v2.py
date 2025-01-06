"""File handling but much nicer way"""
# reading
try:
    with open("module_99_files_v2.txt","r", encoding="utf-8") as file:
        result = file.readlines()
except FileNotFoundError as e:
    print("File not found!")
file.close()

# writing
inputText = input("What would you like to append?")

with open("module_19_files_v2.txt","w", encoding="utf-8") as file:
    file.write(inputText)

file.close()
