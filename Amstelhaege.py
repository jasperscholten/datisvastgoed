import numpy
import random
import matplotlib.pyplot as plt

# 0 = lege ruimte
# 1 = eengezinswoning
# 2 = bungalow
# 3 = maison
# 4 = nu nog standaard vrijstand
# 5 = water

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

    def buildVrijstand(self, x_start, x_end, y_start, y_end, std_vrijstand):
        """
        Add free space on the given location
        """
        # change values in range
        for x in range(x_start - std_vrijstand, x_end + std_vrijstand):
            for y in range(y_start - std_vrijstand, y_end + std_vrijstand):
                self.area[(y, x)] = 4

    def buildWoning(self, x_start, x_end, y_start, y_end, type):
        """
        Build a house on the given location
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

    def createVariables(self, mais, bung, egws):
        maison = dict()
        bungalow = dict()
        singlefam = dict()

        for i in range(mais):
            maison["maison{0}".format(i)] = ['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

        for i in range(bung):
            bungalow["bungalow{0}".format(i)] = ['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

        for i in range(egws):
            singlefam["singlefamily{0}".format(i)] = ['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

        return maison, bungalow, singlefam

    def calculateVrijstand(self, x_lu, y_lu, x_ru, y_ru, x_ld, y_ld, x_rd, y_rd):
        # start search is the corner of the house minus the standard "vrijstand" minus 1 meter

        for each house:
            for each coordinate:
                #valt x coordinaat binnen huis - muur tot muur.
                if x_lu <= x_coordinate <= x_ru:
                    if y_lu <= y_coordinate:
                        distance = abs(y_lu - y_coordinate)
                    else:
                        distance = abs(y_coordinate - y_ld)
                #valt y coordinaat binnen huis - muur tot muur.
                elif y_lu <= y_coordinate <= y_ld:
                    if x_lu <= x_coordinate:
                        distance = abs(x_lu - x_coordinate)
                    else:
                        distance = abs(x_coordinate - x_ru)
                #hoekgevallen
                else:


        return 0


    def calculateValue(self, type, vrijstand):
        '''
        waarde = beginwaarde + vrijstand * procentuele waardevermeerdering per
                    meter * beginwaarde
        '''
        if type == 1:
            value = 285000 + vrijstand * 0.03 * 285000
            return value
        elif type == 2:
            value = 399000 + vrijstand * 0.04 * 399000
            return value
        elif type == 3:
            value = 610000 + vrijstand * 0.06 * 610000
            return value


def initializeSimulation(mais, bung, egws, width, height):
    """
    run the simulation.
    """
    area = ConstructionSite(width, height)
    houses = area.createVariables(mais, bung, egws)

    # build right amount of maisons
    counter = 0
    while counter < mais:
        x_pos = random.randint(0 + 12, width - 22 - 12)
        y_pos = random.randint(0 + 12, height - 21 - 12)
        if area.checkIfPossible(x_pos, x_pos + 22, y_pos, y_pos + 21) == True:
            area.buildVrijstand(x_pos, x_pos + 22, y_pos, y_pos + 21, 12)
            area.buildWoning(x_pos, x_pos + 22, y_pos, y_pos + 21, 3)
            houses[0]["maison{0}".format(counter)][2] = x_pos
            houses[0]["maison{0}".format(counter)][3] = y_pos
            houses[0]["maison{0}".format(counter)][4] = x_pos + 22
            houses[0]["maison{0}".format(counter)][5] = y_pos
            houses[0]["maison{0}".format(counter)][6] = x_pos
            houses[0]["maison{0}".format(counter)][7] = y_pos + 21
            houses[0]["maison{0}".format(counter)][8] = x_pos + 22
            houses[0]["maison{0}".format(counter)][9] = y_pos + 21
            counter += 1


    # build right amount of bungalows
    counter = 0
    while counter < bung:
        x_pos = random.randint(0 + 6, width - 20 - 6)
        y_pos = random.randint(0 + 6, height - 15 - 6)
        if area.checkIfPossible(x_pos, x_pos + 20, y_pos, y_pos + 15) == True:
            area.buildVrijstand(x_pos, x_pos + 20, y_pos, y_pos + 15, 6)
            area.buildWoning(x_pos, x_pos + 20, y_pos, y_pos + 15, 2)
            houses[1]["bungalow{0}".format(counter)][2] = x_pos
            houses[1]["bungalow{0}".format(counter)][3] = y_pos
            houses[1]["bungalow{0}".format(counter)][4] = x_pos + 20
            houses[1]["bungalow{0}".format(counter)][5] = y_pos
            houses[1]["bungalow{0}".format(counter)][6] = x_pos
            houses[1]["bungalow{0}".format(counter)][7] = y_pos + 15
            houses[1]["bungalow{0}".format(counter)][8] = x_pos + 20
            houses[1]["bungalow{0}".format(counter)][9] = y_pos + 15
            counter += 1

    # build right amount of egws
    counter = 0
    while counter < egws:
        x_pos = random.randint(0 + 4, width - 16 - 4)
        y_pos = random.randint(0 + 4, height - 16 - 4)
        if area.checkIfPossible(x_pos, x_pos + 16, y_pos, y_pos + 16) == True:
            area.buildVrijstand(x_pos, x_pos + 16, y_pos, y_pos + 16, 4)
            area.buildWoning(x_pos, x_pos + 16, y_pos, y_pos + 16, 1)
            houses[2]["singlefamily{0}".format(counter)][2] = x_pos
            houses[2]["singlefamily{0}".format(counter)][3] = y_pos
            houses[2]["singlefamily{0}".format(counter)][4] = x_pos + 16
            houses[2]["singlefamily{0}".format(counter)][5] = y_pos
            houses[2]["singlefamily{0}".format(counter)][6] = x_pos
            houses[2]["singlefamily{0}".format(counter)][7] = y_pos + 16
            houses[2]["singlefamily{0}".format(counter)][8] = x_pos + 16
            houses[2]["singlefamily{0}".format(counter)][9] = y_pos + 16
            counter += 1

    # calculateVrijstand and calculateValue for maison
    for i in range(mais):
        x_lu = houses[0]["maison{0}".format(i)][2]
        y_lu = houses[0]["maison{0}".format(i)][3]
        x_ru = houses[0]["maison{0}".format(i)][4]
        y_ru = houses[0]["maison{0}".format(i)][5]
        x_ld = houses[0]["maison{0}".format(i)][6]
        y_ld = houses[0]["maison{0}".format(i)][7]
        x_rd = houses[0]["maison{0}".format(i)][8]
        y_rd = houses[0]["maison{0}".format(i)][9]
        houses[0]["maison{0}".format(i)][1] = area.calculateVrijstand(x_lu, y_lu, x_ru, y_ru, x_ld, y_ld, x_rd, y_rd)
        value = area.calculateValue(3, houses[0]["maison{0}".format(i)][1])
        houses[0]["maison{0}".format(i)][0] = value

    for i in range(bung):
        x_lu = houses[1]["bungalow{0}".format(i)][2]
        y_lu = houses[1]["bungalow{0}".format(i)][3]
        x_ru = houses[1]["bungalow{0}".format(i)][4]
        y_ru = houses[1]["bungalow{0}".format(i)][5]
        x_ld = houses[1]["bungalow{0}".format(i)][6]
        y_ld = houses[1]["bungalow{0}".format(i)][7]
        x_rd = houses[1]["bungalow{0}".format(i)][8]
        y_rd = houses[1]["bungalow{0}".format(i)][9]
        houses[1]["bungalow{0}".format(i)][1] = area.calculateVrijstand(x_lu, y_lu, x_ru, y_ru, x_ld, y_ld, x_rd, y_rd)
        value = area.calculateValue(2, houses[1]["bungalow{0}".format(i)][1])
        houses[1]["bungalow{0}".format(i)][1] = value

    for i in range(egws):
        x_lu = houses[2]["singlefamily{0}".format(i)][2]
        y_lu = houses[2]["singlefamily{0}".format(i)][3]
        x_ru = houses[2]["singlefamily{0}".format(i)][4]
        y_ru = houses[2]["singlefamily{0}".format(i)][5]
        x_ld = houses[2]["singlefamily{0}".format(i)][6]
        y_ld = houses[2]["singlefamily{0}".format(i)][7]
        x_rd = houses[2]["singlefamily{0}".format(i)][8]
        y_rd = houses[2]["singlefamily{0}".format(i)][9]
        houses[2]["singlefamily{0}".format(i)][1] = area.calculateVrijstand(x_lu, y_lu, x_ru, y_ru, x_ld, y_ld, x_rd, y_rd)
        value = area.calculateValue(1, houses[2]["singlefamily{0}".format(i)][1])
        houses[2]["singlefamily{0}".format(i)][0] = value



    print houses


    plt.imshow(area.area)
    #plt.gray()
    plt.show()

initializeSimulation(6, 10, 18 , 300, 320)
