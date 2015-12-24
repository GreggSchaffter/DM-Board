# This is a prototype for DMBoard, or dual-mouse board.

# dm-left.py covers the left mouse, acts as the letter
# selection. This will be done by obtaining the array
# characters from the dm_right object. Then, the index
# of the array chosen will be based off of the mouse
# location checked in this object.

# Import Section:
from pymouse import PyMouse
import dm_right

# Procedure Section:
# Variables
# root - The mouse object that will detect the different locations
#        of the mouse and other aspects for the left mouse.
# screen_width/height - Gets the size of the screen based off of
#                       aspect ratio.
root = PyMouse()
screen_width = root.screen_size()[0]
screen_height = root.screen_size()[1]


# dm_Left Object
class DmLeft:
    # Function Section:
    root.move(screen_width / 2, screen_height / 2)

    def __init__(self):
        """TODO"""
    @property
    def activate(self):
        char_array = dm_right.activate()[1]
        return char_array
