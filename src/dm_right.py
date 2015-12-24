# This is a prototype for DMBoard, or dual-mouse board.

# dm-right.py covers the right mouse, which both
# redirects the cursor to the left mouse for
# selecting a letter and uses the left and right
# mouse button for the space and delete functionality.

# Import Section:

import numpy
import sectCalc

# Procedure Section:
active = True
segments = numpy.array([['a', 'b', 'c', 'd', 'e'],
                        ['f', 'g', 'h', 'i', 'j'],
                        ['k', 'l', 'm', 'n', 'o'],
                        ['p', 'q', 'r', 's', 't'],
                        ['u', 'v', 'w', 'x', 'y'],
                        ['z', '1', '2', '3', '4'],
                        ['5', '6', '7', '8', '9', '0']])


# Function Section:
# This method activates the dm_right object for interpreting
# what string of characters to return.
def activate():
    return mouse_sect_coord()


def mouse_sect_coord():
    return sectCalc.calculate_coord(10, 20)
