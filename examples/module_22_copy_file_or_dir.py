""" Example to copy or move a file or directory """
import os
import shutil

def copy_file(source_file, destination_directory):
    """ Copy a file from source to destination """
    shutil.copy(source_file, destination_directory)

def copy_directory(source_location, destination_location):
    """ Copy a directory from source to destination """
    shutil.copytree(source_location, destination_location)

def move_file(source_file, destination_directory):
    """ Move a file from source to destination """
    shutil.move(source_file, destination_directory)

def move_directory(source_location, destination_location):
    """ Move a directory from source to destination """
    shutil.move(source_location, destination_location)

def rename_file(old_filename, new_name):
    """ Rename a file """
    os.rename(old_filename, new_name)

def remove_file(filename):
    """ Remove a file """
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except OSError as e:
            print('Error: ', e)
    else:
        print('Not a valid file!')

folderSrc = "/tmp/testDirectorySrc/"
folderDst = "/tmp/testDirectoryDst/"

new_file = os.path.join(folderSrc, 'testFile.log')
with open(new_file,"w", encoding="utf-8") as file:
    file.write("What would you like to see here?")

file.close()

copy_file(new_file, folderDst)
remove_file(os.path.join(folderDst, 'testFile.log'))
