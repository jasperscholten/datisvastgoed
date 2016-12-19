import numpy
import random
import math
import matplotlib.pyplot as plt
from copy import deepcopy

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

    def savePositions(self, x_pos, y_pos, length, width):
        positions = ['value', 'vrijstand', x_pos, y_pos, x_pos + length, y_pos, x_pos, y_pos + width, x_pos + length, y_pos + width]
        return positions

    # zorg ervoor dat: a < b, c < d
    def betweenCorners(self, a, b, c, d):
        if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
            return True
        else:
            return False

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

    def getVrijstand(self, currentHouse, houses, type):

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
        if distanceToWall/2.0 < vrijstand:
            #gedeeld door 2 vanwege blokken van 0.5 meter
            vrijstand = distanceToWall/2.0

        if type == 0 and vrijstand < 6:
            return "invalid move"
        if type == 1 and vrijstand < 3:
            return "invalid move"
        if type == 2 and vrijstand < 2:
            return "invalid move"

        return vrijstand

    def calculateValue(self, type, vrijstand):
        '''
        waarde = beginwaarde + vrijstand * procentuele waardevermeerdering per
                    meter * beginwaarde
        '''
        global housevalue
        if type == 2:
            housevalue = 285000 + (vrijstand - 2) * 0.03 * 285000
        elif type == 1:
            housevalue = 399000 + (vrijstand - 3) * 0.04 * 399000
        elif type == 0:
            housevalue = 610000 + (vrijstand - 6) * 0.06 * 610000

        return round(housevalue, 2)

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

    def calculateProvisionalValue(self, houses, type, type_string, firstIndex, i, step):
            housesCopy = deepcopy(houses)

            housesCopy[type][type_string.format(i)][firstIndex] = housesCopy[type][type_string.format(i)][firstIndex] + step
            housesCopy[type][type_string.format(i)][firstIndex + 2] = housesCopy[type][type_string.format(i)][firstIndex + 2] + step
            housesCopy[type][type_string.format(i)][firstIndex + 4] = housesCopy[type][type_string.format(i)][firstIndex + 4] + step
            housesCopy[type][type_string.format(i)][firstIndex + 6] = housesCopy[type][type_string.format(i)][firstIndex + 6] + step

            for i in range(9):
                housesCopy[0]["maison{0}".format(i)][1] = self.getVrijstand(housesCopy[0]["maison{0}".format(i)], housesCopy, 0)
                if housesCopy[0]["maison{0}".format(i)][1] == "invalid move":
                    print "invalid move"
                    return "invalid move"
                housesCopy[0]["maison{0}".format(i)][0] = self.calculateValue(0, housesCopy[0]["maison{0}".format(i)][1])

            for i in range(15):
                housesCopy[1]["bungalow{0}".format(i)][1] = self.getVrijstand(housesCopy[1]["bungalow{0}".format(i)], housesCopy, 1)
                if housesCopy[1]["bungalow{0}".format(i)][1] == "invalid move":
                    print "invalid move"
                    return "invalid move"
                housesCopy[1]["bungalow{0}".format(i)][0] = self.calculateValue(1, housesCopy[1]["bungalow{0}".format(i)][1])

            for i in range(36):
                housesCopy[2]["singlefamily{0}".format(i)][1] = self.getVrijstand(housesCopy[2]["singlefamily{0}".format(i)], housesCopy, 2)
                if housesCopy[2]["singlefamily{0}".format(i)][1] == "invalid move":
                    print "invalid move"
                    return "invalid move"
                housesCopy[2]["singlefamily{0}".format(i)][0] = self.calculateValue(2, housesCopy[2]["singlefamily{0}".format(i)][1])

            return housesCopy

    '''
    Moet ingekort worden.
    '''
    def moveHouse(self, houses, type_string, i, fieldvalue, type):
    # currentHouse = ['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

    # move 1m up
        houses_up = self.calculateProvisionalValue(houses, type, type_string, 3, i, -2)
        if houses_up == "invalid move":
            fieldvalue_up = 0
        else:
            fieldvalue_up = self.totalValue(houses_up)

    # move 1m down
        houses_dwn = self.calculateProvisionalValue(houses, type, type_string, 3, i, 2)
        if houses_dwn == "invalid move":
            fieldvalue_dwn = 0
        else:
            fieldvalue_dwn = self.totalValue(houses_dwn)

    # move 1m to left
        houses_lft = self.calculateProvisionalValue(houses, type, type_string, 2, i, -2)
        if houses_lft == "invalid move":
            fieldvalue_lft = 0
        else:
            fieldvalue_lft = self.totalValue(houses_lft)

    # move 1m to right
        houses_rght = self.calculateProvisionalValue(houses, type, type_string, 2, i, 2)
        if houses_rght == "invalid move":
            fieldvalue_rght = 0
        else:
            fieldvalue_rght = self.totalValue(houses_rght)

        # pick highest value
        newfieldvalue = max([fieldvalue_rght, fieldvalue_lft, fieldvalue_up, fieldvalue_dwn])

        houselist = []
        if newfieldvalue >= fieldvalue:
            if newfieldvalue == fieldvalue_rght:
                houselist.append(houses_rght)
            elif newfieldvalue == fieldvalue_lft:
                houselist.append(houses_lft)
            elif newfieldvalue == fieldvalue_dwn:
                houselist.append(houses_dwn)
            else:
                houselist.append(houses_up)
            return random.choice(houselist)
        else:
            return houses

def initializeSimulation(mais, bung, egws, width, height):
    """
    run the simulation.
    """
    area = ConstructionSite(width, height)
    waterPieces = random.randint(1,4)

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
            if amountWater > 0:
                areaWaterPiece = random.randint(1, amountWater)
        waterRatio = random.randint(1,4)
        sqrtInput = waterRatio * areaWaterPiece
        if sqrtInput < 0:
            sqrtInput = 0
        waterLength = int(round(math.sqrt(sqrtInput)))
        waterWidth = int(round(waterLength / waterRatio))

        x_pos = random.randint(0, width - waterLength)
        y_pos = random.randint(0, height - waterWidth)

        if area.checkIfPossible(x_pos, x_pos + waterLength, y_pos, y_pos + waterWidth) == True:
            area.buildWater(x_pos, x_pos + waterLength, y_pos, y_pos + waterWidth, 5)
            houses[3]["water{0}".format(counter - 1)] = area.savePositions(x_pos, y_pos, waterLength, waterWidth)
            amountWater -= areaWaterPiece
            counter += 1

    # build right amount of maisons
    counter = 0
    while counter < mais:
        x_pos = random.randint(0 + 12, width - 22 - 12)
        y_pos = random.randint(0 + 12, height - 21 - 12)
        if area.checkIfPossible(x_pos, x_pos + 22, y_pos, y_pos + 21) == True:
            area.buildVrijstand(x_pos, x_pos + 22, y_pos, y_pos + 21, 12)
            area.buildWoning(x_pos, x_pos + 22, y_pos, y_pos + 21, 1)
            houses[0]["maison{0}".format(counter)] = area.savePositions(x_pos, y_pos, 22, 21)
            counter += 1

    # build right amount of bungalows
    counter = 0
    while counter < bung:
        x_pos = random.randint(0 + 6, width - 20 - 6)
        y_pos = random.randint(0 + 6, height - 15 - 6)
        if area.checkIfPossible(x_pos, x_pos + 20, y_pos, y_pos + 15) == True:
            area.buildVrijstand(x_pos, x_pos + 20, y_pos, y_pos + 15, 6)
            area.buildWoning(x_pos, x_pos + 20, y_pos, y_pos + 15, 2)
            houses[1]["bungalow{0}".format(counter)] = area.savePositions(x_pos, y_pos, 20, 15)
            counter += 1

    # build right amount of egws
    counter = 0
    while counter < egws:
        x_pos = random.randint(0 + 4, width - 16 - 4)
        y_pos = random.randint(0 + 4, height - 16 - 4)
        if area.checkIfPossible(x_pos, x_pos + 16, y_pos, y_pos + 16) == True:
            area.buildVrijstand(x_pos, x_pos + 16, y_pos, y_pos + 16, 4)
            area.buildWoning(x_pos, x_pos + 16, y_pos, y_pos + 16, 3)
            houses[2]["singlefamily{0}".format(counter)] = area.savePositions(x_pos, y_pos, 16, 16)
            counter += 1

    # calculateVrijstand and calculateValue for maison
    for i in range(mais):
        houses[0]["maison{0}".format(i)][1] = area.getVrijstand(houses[0]["maison{0}".format(i)], houses, 0)
        houses[0]["maison{0}".format(i)][0] = area.calculateValue(0, houses[0]["maison{0}".format(i)][1])

    for i in range(bung):
        houses[1]["bungalow{0}".format(i)][1] = area.getVrijstand(houses[1]["bungalow{0}".format(i)], houses, 1)
        houses[1]["bungalow{0}".format(i)][0] = area.calculateValue(1, houses[1]["bungalow{0}".format(i)][1])

    for i in range(egws):
        houses[2]["singlefamily{0}".format(i)][1] = area.getVrijstand(houses[2]["singlefamily{0}".format(i)], houses, 2)
        houses[2]["singlefamily{0}".format(i)][0] = area.calculateValue(2, houses[2]["singlefamily{0}".format(i)][1])

    # calculate total value of area
    totalvalue = area.totalValue(houses)

    plt.imshow(area.area)
    plt.show()

    return {'totalvalue':totalvalue, 'houses':houses, 'area':area.area}

def randomAlgorithm(runs):
    value60 = []
    value40 = []
    value20 = []

    for i in range(runs):
        print "60 variant"
        value60.append(initializeSimulation(9, 15, 36, 300, 320)['totalvalue'])
        print "40 variant"
        value40.append(initializeSimulation(6, 10, 24, 300, 320)['totalvalue'])
        print "20 variant"
        value20.append(initializeSimulation(3, 5, 12, 300, 320)['totalvalue'])
        print i

    print "Average total value 20:", sum(value20)/float(len(value20))
    print "Average total value 40:", sum(value40)/float(len(value40))
    print "Average total value 60:", sum(value60)/float(len(value60))

    #https://plot.ly/matplotlib/histograms/
    plt.hist(value20)
    plt.title("Average total value 20-houses")
    plt.xlabel("Monetary value ")
    plt.ylabel("Frequency")
    plt.show()

    plt.hist(value40)
    plt.title("Average total value 40-houses")
    plt.xlabel("Monetary value ")
    plt.ylabel("Frequency")
    plt.show()

    plt.hist(value60)
    plt.title("Average total value 60-houses")
    plt.xlabel("Monetary value ")
    plt.ylabel("Frequency")
    plt.show()

    plt.hist(value20)
    plt.hist(value40)
    plt.hist(value60)
    plt.title("Average total value")
    plt.xlabel("Monetary value ")
    plt.ylabel("Frequency")
    plt.show()

def hillClimber(maxMoves, mais, bung, egws):

    result = initializeSimulation(mais, bung, egws, 300, 320)
    houses = result['houses']
    totalvalue = result['totalvalue']
    moves = ConstructionSite(300, 320)

    print "INITIAL", totalvalue

    numberIterations = 0
    nothingChanged = 0

    while nothingChanged < 20 and numberIterations <= maxMoves:
        oldTotalvalue = totalvalue
        # move houses and return houses area with changed values
        for i in range(mais):
            houses = moves.moveHouse(houses, "maison{0}", i, totalvalue, 0)
            totalvalue = moves.totalValue(houses)
        for i in range(bung):
            houses = moves.moveHouse(houses, "bungalow{0}", i, totalvalue, 1)
            totalvalue = moves.totalValue(houses)
        for i in range(egws):
            houses = moves.moveHouse(houses, "singlefamily{0}", i, totalvalue, 2)
            totalvalue = moves.totalValue(houses)

        numberIterations += 1
        print numberIterations, totalvalue

        if totalvalue == oldTotalvalue:
            nothingChanged += 1
        else:
            nothingChanged = 0

    print "FINAL", totalvalue
    #plt.imshow(moves.area)
    #plt.show()

    finalArea = ConstructionSite(300, 320)

    print houses

    for water in range(len(houses[3])):
        waterPiece = houses[3]["water{0}".format(water)]
        finalArea.buildWater(waterPiece[2], waterPiece[4], waterPiece[3], waterPiece[7], 5)

    for housetype in range(3):
        for number in range(len(houses[housetype])):

            if housetype == 2:
                house = houses[housetype]["singlefamily{0}".format(number)]
            elif housetype == 1:
                house = houses[housetype]["bungalow{0}".format(number)]
            else:
                house = houses[housetype]["maison{0}".format(number)]

            finalArea.buildWoning(house[2], house[4], house[3], house[7], (housetype + 1))

    plt.imshow(finalArea.area)
    plt.show()

'''Uncomment algorithm you want to execute'''
# Initialize random configuration
#initializeSimulation(9, 15, 36, 300, 320)
#initializeSimulation(6, 10, 24, 300, 320)
#initializeSimulation(3, 5, 12, 300, 320)
#initializeSimulation(2, 1, 1, 300, 320)

# fill in how many times you want to execute this algorithm
#randomAlgorithm(1)

# 9, 15, 36 /// 6, 10, 24 /// 3, 5, 12
hillClimber(200, 9, 15, 36)
