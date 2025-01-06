""" Example of getting file attributes """

import os
from datetime import datetime

def get_date(timestamp):
    """ Get the date from the timestamp """
    # deprecated: utcfromtimestamp
    # ref: https://discuss.python.org/t/deprecating-utcnow-and-utcfromtimestamp/26221

    result = datetime.utcfromtimestamp(timestamp).strftime('%d %b %Y')
    result = datetime.fromtimestamp(timestamp).strftime('%d %b %Y')
    return result

def get_file_attribs(folder):
    """ List the file attributes """
    with os.scandir(folder) as directory:
        for file in directory:
            if file.is_file():
                information = file.stat()
                print("The file was last modified on: ", get_date(information.st_mtime))

get_file_attribs('/tmp/testDirectorySrc/')
