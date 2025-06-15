"""
Author: Edison Kaulfuss
The three quotes are a special type of comment. Used for larger blocks of comments.
It is also accessable as docstring
Note: it is not by default for comments, it is a multiline quote, but if it is not declared as anything the compiler will ignore it.
"""

from modules import framework2
# The modules subfolder holds all the other py files that you'll create, import them here
import math as m
from math import pi
from math import *
# Here are 3 ways to do imports, for the first you'll need to call it explicitly for access math.pi() or with the as m.pi()
# when using from you can pull single functions and they can be called directly pi()
# with the * you can pull the whole module in like the first method but the functions can be called directly pi(), sum(), etc

def framework():
    # Here is where your app starts often the name main is used, but it is not required
    print("nothing")
    demo = framework2()
    # This is calling the local class in framework 2 as an object called demo. Using demo I can access the functions within the framework2 class



# This dongle indicates what to do if this file is run directly, since this is the main app file it should call the primary function, 
# often main(), but here framework().
if __name__ == "__main__":
    framework()