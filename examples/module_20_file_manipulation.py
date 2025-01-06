""" Examples of file manipulation in Python """
import os

def ends_with_pattern(folder, pattern):
    """ Check the given folder for a specific filename pattern ending"""
    for file in os.listdir(folder):
        if file.endswith(pattern):
            print('File ending with pattern: ', file)
    return True

def starts_with_pattern(folder, pattern):
    """ Check the given folder for a specific filename pattern heading"""
    for file in os.listdir(folder):
        if file.startswith(pattern):
            print('File ending with pattern: ', file)
    return True

def match_for_pattern(folder, pattern):
    """ Check the given folder for a specific filename pattern"""
    for file in os.listdir(folder):
        if file.fnmatch(pattern):
            print('File ending with pattern: ', file)
    return True

# creating directory
folderSrc = "/tmp/testDirectorySrc/"
folderDst = "/tmp/testDirectoryDst/"
try:
    os.mkdir(folderSrc)
    os.mkdir(folderDst)
except FileExistsError as e:
    print('Directory already exists: '+str(e))

new_file = os.path.join(folderSrc, 'testFile.log')

# scanning entries
entries = os.scandir(folderSrc)

# listing files
for entry in entries:
    if os.path.isfile(entry):
        print('File: ', entry.name)
    elif os.path.isdir(entry):
        print('Directory: ', entry.name)

# listing file ending with a specific pattern
ends_with_pattern(folderSrc, '.log')
starts_with_pattern(folderSrc, 'test')
