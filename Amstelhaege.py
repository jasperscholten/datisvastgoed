import numpy
import random
import math
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

    def buildWater(self, x_start, x_end, y_start, y_end, water):
        """
        Build water on the given location
        """
        # change values in range
        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                self.area[(y, x)] = 5

    def checkIfPossible(self, x_start, x_end, y_start, y_end):
        """
        Check if it is possible to build on the given location
        """
        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                if self.area[(y, x)] != 0:
                    return False
        return True

    def createVariables(self, waterPieces, mais, bung, egws):
        water = dict()
        maison = dict()
        bungalow = dict()
        singlefam = dict()

        for i in range(waterPieces):
            water["water{0}".format(i)] = ['x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

        for i in range(mais):
            maison["maison{0}".format(i)] = ['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

        for i in range(bung):
            bungalow["bungalow{0}".format(i)] = ['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

        for i in range(egws):
            singlefam["singlefamily{0}".format(i)] = ['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

        return maison, bungalow, singlefam, water

    # zorg ervoor dat: a < b, c < d
    def betweenCorners(self, a, b, c, d):
        if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
            return True
        else:
            return False

    distance = 0

    # huis 1: ax, ay - huis 2: bx, by
    def pythagoras(self, ax, ay, bx, by):
        length = abs(ax - bx)
        width = abs(ay - by)

        return math.sqrt(length**2 + width**2)

    def calculateVrijstand(self, houses):

        # houses bestaat uit twee arrays, 1 voor het huis dat bekeken wordt, 1 voor een willekeurig ander huis
        # houses = ['value', 'vrijstand', 5, 5, 6, 5, 5, 6, 6, 6], ['value', 'vrijstand', 0, 10, 10, 10, 0, 20, 10, 20]

        # boven
        # huis 1 y_lu >= huis 2 y_ld
        if houses[0][3] >= houses[1][7]:
        # huis 2 x_lu en/of x_ru tussen huis 1 x_lu en x_ru
            if self.betweenCorners(houses[0][2], houses[0][4], houses[1][2], houses[1][4]):
                distance = houses[0][3] - houses[1][7]
                #print "huis boven tussen:", distance
            else:
                # 1_lu, 2_rd
                distance = min(self.pythagoras(houses[0][2], houses[0][3], houses[1][8], houses[1][9]), self.pythagoras(houses[0][4], houses[0][5], houses[1][6], houses[1][7]))
                #print "huis boven hoeken:", distance
        # onder
        # huis 1 y_ld <= huis 2 y_lu
        elif houses[0][7] <= houses[1][3]:
            if self.betweenCorners(houses[0][2], houses[0][4], houses[1][2], houses[1][4]):
                distance = houses[1][3] - houses[0][7]
                #print "huis onder tussen:", distance
            else:
                distance = min(self.pythagoras(houses[0][6], houses[0][7], houses[1][4], houses[1][5]), self.pythagoras(houses[0][8], houses[0][9], houses[1][2], houses[1][3]))
                #print "huis onder hoeken:", distance
        else:
            # left
            if houses[0][2] >= houses[1][4]:
                distance = houses[0][2] - houses[1][4]
                #print "huis links", distance
            # right
            else:
                distance = houses[1][2] - houses[0][4]
                #print "huis rechts", distance

        return distance

    def getVrijstand(self, currentHouse, houses):

        vrijstand = 1000000

        for housetype in range(3):
            for number in range(len(houses[housetype])):

                if housetype == 2:
                    twoHouses = currentHouse, houses[housetype]["singlefamily{0}".format(number)]
                elif housetype == 1:
                    twoHouses = currentHouse, houses[housetype]["bungalow{0}".format(number)]
                else:
                    twoHouses = currentHouse, houses[housetype]["maison{0}".format(number)]

                #gedeeld door 2 vanwege blokken van 0.5 meter
                #vrijstand nauwkeuriger berekenen om preciezere value te krijgen
                currentVrijstand = self.calculateVrijstand(twoHouses)/2.0

                # check if vrijstand is kleiner
                if 0 <= currentVrijstand < vrijstand:
                    vrijstand = currentVrijstand

        # bereken of afstand tot muur kleiner is.
        distanceToWall = min((self.width - currentHouse[8]), (self.height - currentHouse[9]), currentHouse[2], currentHouse[3])
        if distanceToWall < vrijstand:
            #gedeeld door 2 vanwege blokken van 0.5 meter
            vrijstand = distanceToWall/2.0

        return vrijstand

    def calculateValue(self, type, vrijstand):
        '''
        waarde = beginwaarde + vrijstand * procentuele waardevermeerdering per
                    meter * beginwaarde
        '''
        if type == 1:
            value = 285000 + vrijstand * 0.03 * 285000
        elif type == 2:
            value = 399000 + vrijstand * 0.04 * 399000
        elif type == 3:
            value = 610000 + vrijstand * 0.06 * 610000

        return round(value, 2)

    def totalValue(self, houses):

        value = 0

        for housetype in range(3):
            for number in range(len(houses[housetype])):

                if housetype == 2:
                    value += houses[housetype]["singlefamily{0}".format(number)][0]
                elif housetype == 1:
                    value += houses[housetype]["bungalow{0}".format(number)][0]
                else:
                    value += houses[housetype]["maison{0}".format(number)][0]

        return value

def initializeSimulation(mais, bung, egws, width, height):
    """
    run the simulation.
    """
    area = ConstructionSite(width, height)
    waterPieces = random.randint(1,4)
    waterRatio = random.randint(1,4)
    amountWater = 19200
    houses = area.createVariables(waterPieces, mais, bung, egws)

    # build right amount of water pieces
    counter = 1
    waterLength = 0
    waterWidth = 0
    while counter <= waterPieces:
        if counter == waterPieces:
            areaWaterPiece = amountWater
        else:
            areaWaterPiece = random.randint(1, amountWater)

        waterLength = int(round(math.sqrt(waterRatio * areaWaterPiece)))
        waterWidth = int(round(waterLength / waterRatio))
        x_pos = random.randint(0, width - waterLength)
        y_pos = random.randint(0, height - waterWidth)

        if area.checkIfPossible(x_pos, x_pos + waterLength, y_pos, y_pos + waterWidth) == True:
            area.buildWater(x_pos, x_pos + waterLength, y_pos, y_pos + waterWidth, 5)
            houses[3]["water{0}".format(counter - 1)][0] = x_pos
            houses[3]["water{0}".format(counter - 1)][1] = y_pos
            houses[3]["water{0}".format(counter - 1)][2] = x_pos + waterLength
            houses[3]["water{0}".format(counter - 1)][3] = y_pos
            houses[3]["water{0}".format(counter - 1)][4] = x_pos
            houses[3]["water{0}".format(counter - 1)][5] = y_pos + waterWidth
            houses[3]["water{0}".format(counter - 1)][6] = x_pos + waterLength
            houses[3]["water{0}".format(counter - 1)][7] = y_pos + waterWidth
            amountWater -= areaWaterPiece
            counter += 1
            print ("size:", areaWaterPiece)

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
        houses[0]["maison{0}".format(i)][1] = area.getVrijstand(houses[0]["maison{0}".format(i)], houses)
        houses[0]["maison{0}".format(i)][0] = area.calculateValue(3, houses[0]["maison{0}".format(i)][1])

    for i in range(bung):
        houses[1]["bungalow{0}".format(i)][1] = area.getVrijstand(houses[1]["bungalow{0}".format(i)], houses)
        houses[1]["bungalow{0}".format(i)][0] = area.calculateValue(2, houses[1]["bungalow{0}".format(i)][1])

    for i in range(egws):
        houses[2]["singlefamily{0}".format(i)][1] = area.getVrijstand(houses[2]["singlefamily{0}".format(i)], houses)
        houses[2]["singlefamily{0}".format(i)][0] = area.calculateValue(1, houses[2]["singlefamily{0}".format(i)][1])

    print houses
    print "Total Value:", area.totalValue(houses)

    plt.imshow(area.area)
    #plt.gray()
    plt.show()

initializeSimulation(9, 15, 36, 300, 320)
#initializeSimulation(6, 10, 24, 300, 320)
#initializeSimulation(3, 5, 12, 300, 320)
#initializeSimulation(2, 1, 1, 300, 320)
