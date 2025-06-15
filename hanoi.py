"""
Author: Edison Kaulfuss
This is just me playing with the concept of the Tower of Hanoi
"""

from board import board

# The Tower of Hanoi has 3 rules
# Only 1 move at a time
# A move consists of moving the upper disk from a stack and placing it on another stack or empty rod
# No disk may be placed on any smaller disk
# We will be representing rods with lists and disks with numbers 1-n


def main():
    b = board()

    while True:
        # pop(0) is all you can do and insert(0, inHand)

        #inHand = rod1.pop(0)
        #rod2.insert(0, inHand)

        try:
            if b.getRod(1)[0] > b.getRod(2)[0]:
                b.doSwap(2,1)
            else:
                b.doSwap(1,2)
        except:
            if len(b.getRod(1)) == 0: b.doSwap(2,1)
            if len(b.getRod(2)) == 0: b.doSwap(1,2)
        
        b.showMe()
        if b.getRod(2) == [1,2,3,4,5,6,7,8]: break

        try:
            if b.getRod(1)[0] > b.getRod(3)[0]:
                b.doSwap(3,1)
            else:
                b.doSwap(1,3)
        except:
            if len(b.getRod(1)) == 0: b.doSwap(3,1)
            if len(b.getRod(3)) == 0: b.doSwap(1,3)

        b.showMe()

        try:
            if b.getRod(2)[0] > b.getRod(3)[0]:
                b.doSwap(3,2)
            else:
                b.doSwap(2,3)
        except:
            if len(b.getRod(2)) == 0: b.doSwap(3,2)
            if len(b.getRod(3)) == 0: b.doSwap(2,3)

        b.showMe()

        if b.getRod(3) == [1,2,3,4,5,6,7,8]: break




if __name__ == "__main__":
    main()