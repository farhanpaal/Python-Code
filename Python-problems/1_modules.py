"""
A module is a Python file that contains functions, which can be used in other files by importing the module.
It helps keep code organized and reusable.

In this example, we will create 2 files:
1) Module file : action.py
2) Project file: code.py
"""

# --------------------------
# 1) action.py
def get(a):
    print(a)

def set(b):
    c = input(b)  # ask user for input
    print(c)



# --------------------------
# 2) code.py (run this file)
from action import get, set  

def app():
    get("Our program")      # prints message
    set("Enter name: \n")   # asks input from user and prints it

app()

"""
output:
Our program
Enter name: _____
_____
"""
