"""
Author: Edison Kaulfuss
The three quotes are a special type of comment. Used for larger blocks of comments.
It is also accessable as docstring
Note: it is not by default for comments, it is a multiline quote, but if it is not declared as anything the compiler will ignore it.
"""
class framework2():
    
    # TODO: adding TODO to a comment will highlight it in some IDEs, useful for pseudocode
    # class variables
    aNumber = 0

    def __init__(self, aNumber = 1):
        # This is your class constructor method
        # if this constructor is called with a number aNumber will be set to that otherwise it is set to 1
        # pass is used as a place holder, it just prevents empty functions from causing errors
        pass

    def getANumber(self):
        # This is a getter all it does is provide indirect access to the variables in the class
        return self.aNumber

    def setANumber(self, num):
        # this is a setter it is passed self and a number and sets the variable to that.
        self.aNumber = num
    
    def doStuff(self):
        # generic class application stuff is done here
        pass



if __name__ == "__main__":
    # This is the instruction for what to do if this file is run by itself
    print("Please run the framework.py file, this file is not standalone.")