# modules/__init__.py
"""
In older versions of Python (before 3.3), the presence of an __init__.py file 
in a directory was required for Python to treat that directory as a package. 

Without it, Python wouldn’t recognize the folder as a module and would be 
unable to import files from it.

In modern Python (3.3 and above), it’s no longer mandatory, but it's still a 
good practice to include it to indicate that the directory should be 
treated as a package.
"""
