# This is a prototype for DMBoard, or dual-mouse board.

# sectCalc.py does the calculations for obtaining which sector
# that the mouse position is located in. This will be determined
# by first obtaining which mouse this calculation is being done
# for. Then, it will do the proper calculations based off of
# the inputted position. It will return the sector after such
# calculation is done.

# Import Section:

from pymouse import PyMouse
import numpy
import math

# Procedure Section:
active = True
root = PyMouse()
delta_x = 0
delta_y = 0


# Function Section:
# calculatedCoord - Calculates the vector value to return to the
#                   dm_left/right objects.
def calculate_coord(inner_r, outer_r):
    # Variables:
    # screen_center - An array that contains center vertex, x being 0 and 1 being y
    # vector_val - Stores the vertex value associated with the coordinate. Calculated
    #              by the equation sqrrt[delta_x^2 + delta_^2](distance).
    # delta_x - The difference between mouse position x and screen_center x.
    # delta_y - The difference between mouse positin y and screen center y.
    screen_center = numpy.array([root.screen_size()[0] / 2, root.screen_size()[1] / 2])
    vector_val = 0
    sect = 0
    update_mouse_diff(screen_center)
    while active:
        vector_val_q = vector_val
        if inner_r < vector_val < outer_r:
            if int(root.position()[1]) - screen_center[1] < 0:
                if int(root.position()[0]) - screen_center[0] < 0:
                    sect += 1
            elif int(root.position()[1]) - screen_center[1] > 0:
                sect += 2
                if root.position()[0] - screen_center[0] > 0:
                    sect += 1
            return vector_val, sect
        update_mouse_diff(screen_center)
        vector_val = math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))


# determineSection - Determines which section, based on side, was selected by the
#                    focused mouse area.
# Parameters - side: If 0, left mouse. if 1, right mouse.
#              vector: The vector value associated with the data received.
#              sect: The section in the coordinate plane that the vector is located
#                    in.
def determine_section(side, vector, sect):
    """ TODO: Enter code here """


def update_mouse_diff(pos):
    global delta_x, delta_y
    delta_x = int(root.position()[0]) - pos[0]
    delta_y = int(root.position()[1]) - pos[1]
