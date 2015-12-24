# This is a prototype for DMBoard, or dual-mouse board.

# dm-layout.py is the code that sets up the "board" for
# the two mice, configuring the cursor to react to the
# different locations of the mice.

# Import Section:

from dm_left import DmLeft

# Procedure Section:
active = True
base = DmLeft()
char = ''
while active:
    active = False
    char = base.activate
print char
# Function Section:

"""TODO: Enter import stuff here"""
