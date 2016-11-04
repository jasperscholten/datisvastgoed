import numpy
import random
import matplotlib.pyplot as plt


class ConstructionSite(object):
    """
    The Construction is a rectangular form where the houses are build.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # make width and height global variables
        self.width = width
        self.height = height
        # initializes an 2d array
        self.area = numpy.zeros((height, width), dtype='int32')
    def buildWoning(self, x_start, x_end, y_start, y_end, type):
        """
        Build the eensgezinswoning on the given location
        """
        # change values in range
        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                self.area[(y, x)] = type
    def checkIfPossible(self, x_start, x_end, y_start, y_end):
        """
        Check if it is possible to build on the given location
        """
        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                if self.area[(y, x)] != 0:
                    return False
        return True

class Eensgezinswoning(object):
    """
    A house with with 8m x 8m --> 16 x 16 tiles.
    """
    def __init__(self):
        self.egw_width = 16
        self.egw_length = 16

def RunSimulation(mais, bung, egws, width, height):
    """
    run the simulation.
    """
    area = ConstructionSite(width, height)

    # build right amount of maisons
    counter = 0
    while counter < mais:
        x_pos = random.randint(0, width - 20)
        y_pos = random.randint(0, height - 15)
        if area.checkIfPossible(x_pos, x_pos + 20, y_pos, y_pos + 15) == True:
            area.buildWoning(x_pos, x_pos + 20, y_pos, y_pos + 15, 1)
            counter += 1

    # build right amount of bungalows
    counter = 0
    while counter < bung:
        x_pos = random.randint(0, width - 22)
        y_pos = random.randint(0, height - 21)
        if area.checkIfPossible(x_pos, x_pos + 22, y_pos, y_pos + 21) == True:
            area.buildWoning(x_pos, x_pos + 22, y_pos, y_pos + 21, 2)
            counter += 1

    # build right amount of egws
    counter = 0
    while counter < egws:
        x_pos = random.randint(0, width - 16)
        y_pos = random.randint(0, height - 16)
        if area.checkIfPossible(x_pos, x_pos + 16, y_pos, y_pos + 16) == True:
            area.buildWoning(x_pos, x_pos + 16, y_pos, y_pos + 16, 3)
            counter += 1
    plt.imshow(area.area)
    #plt.gray()
    plt.show()



RunSimulation(4, 5, 6, 300, 320)

plt.imshow(area.area)
#plt.gray()
plt.show()
