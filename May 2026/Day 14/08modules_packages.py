""""
1. What are modules and packages?
Module-- A single Python file (.py) that contains code (functions, classes, variables).
Example: a file named calculator.py is a module.

Package-- A folder that contains multiple modules and a special __init__.py file. It groups related modules together.
Example: a folder utilities/ with files math_tools.py and string_tools.py is a package.

Why bother?

Organization--Keep related code together.

Reusability--Write a function once, import it anywhere.

Namespacing-- Avoid name clashes (two modules can have a function with the same name).
"""


import os
import datetime
import math

print(math.sqrt(25))  # 5.0

print(os.getcwd())                     # current working directory
print(datetime.datetime.now())        # current date and time

import mymodule

print(mymodule.greet("Rehman"))  # Hello, Rehman!
print(mymodule.PI)              # 3.14159

import sys
print(sys.path)