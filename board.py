"""
Author: Edison Kaulfuss
Class to hold the board of rods
"""
import os
import time

class board():
    
    # TODO: adding TODO to a comment will highlight it in some IDEs, useful for pseudocode
    # class variables
    rods = [[1,2,3,4,5,6,7,8],[],[]]

    def __init__(self):
        pass

    def getRod(self, whichOne):
        # This is a getter all it does is provide indirect access to the variables in the class
        return self.rods[whichOne - 1]
    
        
    def doSwap(self, fromRod, toRod):
        self.rods[toRod - 1].insert(0, self.rods[fromRod - 1].pop(0))

    def showMe(self):
        time.sleep(0.1)
        os.system('cls')
        print(self.getRod(1))
        print(self.getRod(2))
        print(self.getRod(3))


if __name__ == "__main__":
    # This is the instruction for what to do if this file is run by itself
    print("Please run the hanoi.py file, this file is not standalone.")