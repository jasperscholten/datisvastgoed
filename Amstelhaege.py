import numpy
import random
import math
import time
import matplotlib.pyplot as plt
from copy import deepcopy
import csv
import sys

variantArray = []
totalvalueArray = []
vrijstandArray = []
waterPiecesArray = []
waterareaArray = []

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
        for x in range(x_start - std_vrijstand - 1, x_end + std_vrijstand):
            for y in range(y_start - std_vrijstand - 1, y_end + std_vrijstand):
                self.area[(y, x)] = 4

    def buildWoning(self, x_start, x_end, y_start, y_end, type):
        """
        Build a house or water on the given location
        """
        # change values in range
        for x in range(x_start - 1, x_end):
            for y in range(y_start - 1, y_end):
                self.area[(y, x)] = type

    def checkIfPossible(self, x_start, x_end, y_start, y_end):
        """
        Check if it is possible to build on the given location
        """
        for x in range(x_start - 1, x_end):
            for y in range(y_start - 1, y_end):
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

    def savePositions(self, x_pos, y_pos, leng, wid):
        positions = ['value', 'vrijstand', x_pos, y_pos, x_pos + leng, y_pos, x_pos, y_pos + wid, x_pos + leng, y_pos + wid]
        return positions

    # zorg ervoor dat: a < b, c < d
    def betweenCorners(self, a, b, c, d):
        if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
            return True
        else:
            return False

    # huis 1: ax, ay - huis 2: bx, by
    def pythagoras(self, ax, ay, bx, by):
        leng = abs(ax - bx)
        wid = abs(ay - by)

        return math.sqrt(leng**2 + wid**2)

    def calculateVrijstand(self, houses):

        # houses bestaat uit twee arrays, 1 voor het huis dat bekeken wordt, 1 voor een willekeurig ander huis

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

        for i in range(len(houses[3])):
            if self.betweenCorners(houses[3]["water{0}".format(i)][2], houses[3]["water{0}".format(i)][4],  currentHouse[2],  currentHouse[4]):
                if self.betweenCorners(houses[3]["water{0}".format(i)][3], houses[3]["water{0}".format(i)][7],  currentHouse[3],  currentHouse[7]):
                    return "invalid move"

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

    def totalValue(self, houses, index):
        value = 0

        for housetype in range(3):
            for number in range(len(houses[housetype])):

                if housetype == 2:
                    value += houses[housetype]["singlefamily{0}".format(number)][index]
                elif housetype == 1:
                    value += houses[housetype]["bungalow{0}".format(number)][index]
                else:
                    value += houses[housetype]["maison{0}".format(number)][index]

        return value

    def calculateProvisionalValue(self, variant, houses, type, type_string, firstIndex, i, step):
            housesCopy = deepcopy(houses)

            housesCopy[type][type_string.format(i)][firstIndex] = housesCopy[type][type_string.format(i)][firstIndex] + step
            housesCopy[type][type_string.format(i)][firstIndex + 2] = housesCopy[type][type_string.format(i)][firstIndex + 2] + step
            housesCopy[type][type_string.format(i)][firstIndex + 4] = housesCopy[type][type_string.format(i)][firstIndex + 4] + step
            housesCopy[type][type_string.format(i)][firstIndex + 6] = housesCopy[type][type_string.format(i)][firstIndex + 6] + step

            box = 320
            if variant == 60:
                box = 50
            elif variant == 40:
                box = 75
            else:
                box = 100

            x_lu = housesCopy[type][type_string.format(i)][2] - box
            x_ru = housesCopy[type][type_string.format(i)][4] + box
            y_lu = housesCopy[type][type_string.format(i)][3] - box
            y_ld = housesCopy[type][type_string.format(i)][7] + box

            for i in range(len(housesCopy[0])):
                selected = housesCopy[0]["maison{0}".format(i)]
                if x_lu < (selected[2] or selected[4]) < x_ru and y_lu < (selected[3] or selected[7]) < y_ld:
                    selected[1] = self.getVrijstand(selected, housesCopy, 0)
                    if selected[1] == "invalid move":
                        return "invalid move"
                    selected[0] = self.calculateValue(0, selected[1])

            for i in range(len(housesCopy[1])):
                selected = housesCopy[1]["bungalow{0}".format(i)]
                if x_lu < (selected[2] or selected[4]) < x_ru and y_lu < (selected[3] or selected[7]) < y_ld:
                    selected[1] = self.getVrijstand(selected, housesCopy, 1)
                    if selected[1] == "invalid move":
                        return "invalid move"
                    selected[0] = self.calculateValue(1, selected[1])

            for i in range(len(housesCopy[2])):
                selected = housesCopy[2]["singlefamily{0}".format(i)]
                if x_lu < (selected[2] or selected[4]) < x_ru and y_lu < (selected[3] or selected[7]) < y_ld:
                    selected[1] = self.getVrijstand(selected, housesCopy, 2)
                    if selected[1] == "invalid move":
                        return "invalid move"
                    selected[0] = self.calculateValue(2, selected[1])

            return housesCopy

    def moveHouse(self, variant, houses, type_string, i, fieldvalue, type, optimalisatietype):

    # move 1m up
        houses_up = self.calculateProvisionalValue(variant, houses, type, type_string, 3, i, -2)
        if houses_up == "invalid move":
            fieldvalue_up = 0
        else:
            fieldvalue_up = self.totalValue(houses_up, optimalisatietype)

    # move 1m down
        houses_dwn = self.calculateProvisionalValue(variant, houses, type, type_string, 3, i, 2)
        if houses_dwn == "invalid move":
            fieldvalue_dwn = 0
        else:
            fieldvalue_dwn = self.totalValue(houses_dwn, optimalisatietype)

    # move 1m to left
        houses_lft = self.calculateProvisionalValue(variant, houses, type, type_string, 2, i, -2)
        if houses_lft == "invalid move":
            fieldvalue_lft = 0
        else:
            fieldvalue_lft = self.totalValue(houses_lft, optimalisatietype)

    # move 1m to right
        houses_rght = self.calculateProvisionalValue(variant, houses, type, type_string, 2, i, 2)
        if houses_rght == "invalid move":
            fieldvalue_rght = 0
        else:
            fieldvalue_rght = self.totalValue(houses_rght, optimalisatietype)

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
            return {'houses': random.choice(houselist), 'totalvalue': newfieldvalue}
        else:
            return {'houses': houses, 'totalvalue': fieldvalue}

    def moveHouseSA(self, variant, houses, type_string, i, fieldvalue, type):
        houses_move = self.calculateProvisionalValue(variant, houses, type, type_string, random.choice([2,3]), i, random.choice([-2,2]))
        if houses_move == "invalid move":
            return {'houses': houses, 'totalvalue': fieldvalue}
        else:
            fieldvalue_move = self.totalValue(houses_move, 0)
        return {'houses': houses_move, 'totalvalue': fieldvalue_move}

    def pickHouseSA(self, mais, bung, egws):
        type_string = random.choice(["maison{0}","bungalow{0}","singlefamily{0}"])
        i = 0
        housetype = 0
        if type_string == "maison{0}":
            i = random.randint(0, mais - 1)
            housetype = 0
        elif type_string == "bungalow{0}":
            i = random.randint(0, bung - 1)
            housetype = 1
        else:
            i = random.randint(0, egws - 1)
            housetype = 2

        return {'type_string': type_string, 'i': i, 'housetype': housetype}

    def acceptanceProbability(self, old, new, T):
        return math.e ** ((float(old) - float(new))/float(T))

def visualizeArea(houses):
    area = ConstructionSite(300, 320)

    for water in range(len(houses[3])):
        waterPiece = houses[3]["water{0}".format(water)]
        area.buildWoning(waterPiece[2], waterPiece[4], waterPiece[3], waterPiece[7], 5)

    for housetype in range(3):
        for number in range(len(houses[housetype])):

            if housetype == 2:
                house = houses[housetype]["singlefamily{0}".format(number)]
            elif housetype == 1:
                house = houses[housetype]["bungalow{0}".format(number)]
            else:
                house = houses[housetype]["maison{0}".format(number)]

            area.buildWoning(house[2], house[4], house[3], house[7], (housetype + 1))

    plt.imshow(area.area)
    plt.show()

def createArrays(variant, totalvalue, vrijstand, waterPieces, waterarea):
    """
    create an Excel file for the amount of water pieces in the simulations.
    """

    variantArray.append(variant)
    totalvalueArray.append(totalvalue)
    vrijstandArray.append(vrijstand)
    waterPiecesArray.append(waterPieces)
    waterareaArray.append(waterarea)

def createFile(variantArray, totalvalueArray , vrijstandArray, waterPiecesArray, waterareaArray, rows, filename):
    f = open("datisvastgoed\%s.csv" % filename, 'wb')

    writer = csv.writer(f)
    writer.writerow(('variant', 'Totalvalue', 'Vrijstand', 'waterPieces', 'waterarea'))
    for i in range(rows):
        writer.writerow((variantArray[i], totalvalueArray[i], vrijstandArray[i], waterPiecesArray[i], waterareaArray[i]))
    f.close

def saveHighest(houses20, houses40, houses60, value20, value40, value60, filename):
    text_file = open("datisvastgoed\%s.txt" % filename, "w")
    text_file.writelines(["20 houses:", "\n", str(value20), "\n", str(houses20), "\n", "40 houses:", "\n", str(value40), "\n", str(houses40), "\n", "60 houses:", "\n", str(value60), "\n", str(houses60)])
    text_file.close()

def printHistogram(value20, value40, value60):
    print "Average total value 20:", sum(value20)/float(len(value20))
    print "Average total value 40:", sum(value40)/float(len(value40))
    print "Average total value 60:", sum(value60)/float(len(value60))

    #https://plot.ly/matplotlib/histograms/
    plt.hist(value20)
    plt.title("Average total value 20-houses")
    plt.xlabel("Monetary value")
    plt.ylabel("Frequency")
    plt.show()

    plt.hist(value40)
    plt.title("Average total value 40-houses")
    plt.xlabel("Monetary value")
    plt.ylabel("Frequency")
    plt.show()

    plt.hist(value60)
    plt.title("Average total value 60-houses")
    plt.xlabel("Monetary value")
    plt.ylabel("Frequency")
    plt.show()

    plt.hist(value20)
    plt.hist(value40)
    plt.hist(value60)
    plt.title("Average total value")
    plt.xlabel("Monetary value")
    plt.ylabel("Frequency")
    plt.show()

def createField(area, waterPieces, houses, mais, bung, egws, width, height):
    timer = time.time() + 2

    # build right amount of water pieces
    counter = 1
    amountWater = 19200
    waterLength = 0
    waterWidth = 0
    waterarea = []
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
            area.buildWoning(x_pos, x_pos + waterLength, y_pos, y_pos + waterWidth, 5)
            houses[3]["water{0}".format(counter - 1)] = area.savePositions(x_pos, y_pos, waterLength, waterWidth)
            amountWater -= areaWaterPiece
            waterarea.append(areaWaterPiece)
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
        if time.time() > timer:
            print 'restart'
            return 'start'

    return {'area': area, 'houses': houses, 'waterarea': waterarea}

def initializeSimulation(mais, bung, egws, width, height):
    """
    run the simulation.
    """

    result = 'start'
    while result == 'start':
        area = ConstructionSite(width, height)
        waterPieces = random.randint(1,4)
        houses = area.createVariables(waterPieces, mais, bung, egws)
        result = createField(area, waterPieces, houses, mais, bung, egws, width, height)

    area = result['area']
    houses = result['houses']

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
    totalvalue = area.totalValue(houses, 0)
    vrijstand = area.totalValue(houses, 1)

    #plt.imshow(area.area)
    #plt.show()

    return {'totalvalue':totalvalue, 'houses':houses, 'area':area.area, 'vrijstand': vrijstand, 'waterPieces': waterPieces, 'waterarea': result['waterarea'] }

def randomAlgorithm(runs, filename):
    value60 = []
    value40 = []
    value20 = []
    highestValue60 = 0
    highestValue40 = 0
    highestValue20 = 0

    for i in range(runs):
        result = initializeSimulation(9, 15, 36, 300, 320)
        value60.append(result['totalvalue'])
        if result['totalvalue'] > highestValue60:
            highestValue60 = result['totalvalue']
            highestHouses60 = result['houses']
        createArrays(60, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])
        result = initializeSimulation(6, 10, 24, 300, 320)
        value40.append(result['totalvalue'])
        if result['totalvalue'] > highestValue40:
            highestValue40 = result['totalvalue']
            highestHouses40 = result['houses']
        createArrays(40, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])
        result = initializeSimulation(3, 5, 12, 300, 320)
        value20.append(result['totalvalue'])
        if result['totalvalue'] > highestValue20:
            highestValue20 = result['totalvalue']
            highestHouses20 = result['houses']
        createArrays(20, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])
        print i

    createFile(variantArray, totalvalueArray , vrijstandArray, waterPiecesArray, waterareaArray, runs * 3, filename)
    saveHighest(highestHouses20, highestHouses40, highestHouses60, highestValue20, highestValue40, highestValue60, filename)
    printHistogram(value20, value40, value60)

def hillClimber(maxMoves, variant, visualize, optimalisatietype):
    mais = int(variant * 0.15)
    bung = int(variant * 0.25)
    egws = int(variant * 0.6)

    result = initializeSimulation(mais, bung, egws, 300, 320)
    waterPieces = result['waterPieces']
    waterarea = result['waterarea']
    houses = result['houses']
    totalvalue = result['totalvalue']
    moves = ConstructionSite(300, 320)
    numberIterationsArray = []
    totalvalueArray = []

    print "INITIAL", totalvalue

    numberIterations = 0
    nothingChanged = 0

    while nothingChanged < 10 and numberIterations <= maxMoves:
        oldTotalvalue = totalvalue
        # move houses and return houses area with changed values
        for i in range(mais):
            result = moves.moveHouse(variant, houses, "maison{0}", i, totalvalue, 0, optimalisatietype)
            houses = result['houses']
            totalvalue = result['totalvalue']
        for i in range(bung):
            result = moves.moveHouse(variant, houses, "bungalow{0}", i, totalvalue, 1, optimalisatietype)
            houses = result['houses']
            totalvalue = result['totalvalue']
        for i in range(egws):
            result = moves.moveHouse(variant, houses, "singlefamily{0}", i, totalvalue, 2, optimalisatietype)
            houses = result['houses']
            totalvalue = result['totalvalue']

        numberIterations += 1
        print numberIterations, totalvalue
        numberIterationsArray.append(numberIterations)
        totalvalueArray.append(totalvalue)

        if totalvalue == oldTotalvalue:
            nothingChanged += 1
        else:
            nothingChanged = 0

    print "FINAL", totalvalue

    plt.plot(numberIterationsArray,totalvalueArray)
    plt.xlabel('Number of iterations')
    plt.ylabel('Total value')
    #plt.show()

    if visualize == 'yes':
        visualizeArea(houses)

        #print numberIterationsArray, totalvalueArray
        plt.plot(numberIterationsArray,totalvalueArray)
        plt.xlabel('number Iterations')
        plt.ylabel('total value')
        plt.show()

    finalArea = ConstructionSite(300, 320)
    totalvalue = moves.totalValue(houses, 0)
    vrijstand = moves.totalValue(houses, 1)

    return {'totalvalue': totalvalue, 'vrijstand': vrijstand, 'waterPieces': waterPieces, 'waterarea': waterarea, 'houses': houses}

def repeatHillClimber(runs, filename, optimalisatietype):
    value60 = []
    value40 = []
    value20 = []
    highestValue60 = 0
    highestValue40 = 0
    highestValue20 = 0

    for i in range(runs):
        print i
        print "60 variant"
        result = hillClimber(200, 60, 'no', optimalisatietype)
        value60.append(result['totalvalue'])
        if result['totalvalue'] > highestValue60:
            highestValue60 = result['totalvalue']
            highestHouses60 = result['houses']
        createArrays(60, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])
        print "40 variant"
        result = hillClimber(200, 40, 'no', optimalisatietype)
        value40.append(result['totalvalue'])
        if result['totalvalue'] > highestValue40:
            highestValue40 = result['totalvalue']
            highestHouses40 = result['houses']
        createArrays(40, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])
        print "20 variant"
        result = hillClimber(200, 20, 'no', optimalisatietype)
        value20.append(result['totalvalue'])
        if result['totalvalue'] > highestValue20:
            highestValue20 = result['totalvalue']
            highestHouses20 = result['houses']
        createArrays(20, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])

    createFile(variantArray, totalvalueArray , vrijstandArray, waterPiecesArray, waterareaArray, runs * 3, filename)
    saveHighest(highestHouses20, highestHouses40, highestHouses60, highestValue20, highestValue40, highestValue60, filename)

    plt.hist(value20)
    plt.title("Initializing Histogram")
    plt.xlabel("Close for right Histograms")
    plt.ylabel("")
    plt.show()

    printHistogram(value20, value40, value60)

#http://katrinaeg.com/simulated-annealing.html
def simulatedAnnealing(variant, T, T_min, alpha, maxIterations, visualize):
    mais = int(variant * 0.15)
    bung = int(variant * 0.25)
    egws = int(variant * 0.6)

    initialResult = initializeSimulation(mais, bung, egws, 300, 320)
    houses = initialResult['houses']
    totalvalue = initialResult['totalvalue']
    waterPieces = initialResult['waterPieces']
    waterarea = initialResult['waterarea']
    highestValue = totalvalue
    oldCost = totalvalue/100000.0
    moves = ConstructionSite(300, 320)

    print "INITIAL:", totalvalue

    while T > T_min:
        iteration = 1
        while iteration <= maxIterations:
            pick = moves.pickHouseSA(mais, bung, egws)
            result = moves.moveHouseSA(variant, houses, pick['type_string'], pick['i'], totalvalue, pick['housetype'], optimalisatietype)
            newHouses = result['houses']
            newTotalValue = result['totalvalue']
            newCost = newTotalValue/100000.0
            ap = moves.acceptanceProbability(oldCost, newCost, T)

            if ap > random.random():
                houses = newHouses
                totalvalue = newTotalValue
                oldCost = newCost

                if totalvalue > highestValue:
                    highestValue = totalvalue
            iteration += 1
        print T
        T = T*alpha

    vrijstand = moves.totalValue(houses, 1)
    print "FINAL:", totalvalue
    print "HIGHEST:", highestValue

    if visualize == 'yes':
        visualizeArea(houses)

    return {'totalvalue': totalvalue, 'vrijstand': vrijstand, 'waterPieces': waterPieces, 'waterarea': waterarea, 'houses': houses}

def repeatSimulatedAnnealing(runs, filename):
    value60 = []
    value40 = []
    value20 = []
    highestValue60 = 0
    highestValue40 = 0
    highestValue20 = 0

    for i in range(runs):
        print i
        print "60 variant"
        result = simulatedAnnealing(60, 1.0, 0.0002, 0.99, 50, 'no')
        value60.append(result['totalvalue'])
        if result['totalvalue'] > highestValue60:
            highestValue60 = result['totalvalue']
            highestHouses60 = result['houses']
        createArrays(60, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])
        print "40 variant"
        result = simulatedAnnealing(40, 1.0, 0.0002, 0.99, 50, 'no')
        value40.append(result['totalvalue'])
        if result['totalvalue'] > highestValue40:
            highestValue40 = result['totalvalue']
            highestHouses40 = result['houses']
        createArrays(40, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])
        print "20 variant"
        result = simulatedAnnealing(20, 1.0, 0.0002, 0.99, 50, 'no')
        value20.append(result['totalvalue'])
        if result['totalvalue'] > highestValue20:
            highestValue20 = result['totalvalue']
            highestHouses20 = result['houses']
        createArrays(20, result['totalvalue'], result['vrijstand'], result['waterPieces'], result['waterarea'])

    createFile(variantArray, totalvalueArray , vrijstandArray, waterPiecesArray, waterareaArray, runs * 3, filename)
    saveHighest(highestHouses20, highestHouses40, highestHouses60, highestValue20, highestValue40, highestValue60, filename)

    plt.hist(value20)
    plt.title("Initializing Histogram")
    plt.xlabel("Close for right Histograms")
    plt.ylabel("")
    plt.show()

    printHistogram(value20, value40, value60)

'''Algorithms'''

def integerInput(text):
    while True:
        try:
            integer = int(raw_input(text))
        except ValueError:
            print("\n ### Choose a valid integer as type ###\n")
            continue
        else:
            return integer

def runProgram():
    print "\n\n### AMSTELHAEGE - DATISVASTGOED B.V. ###\n\n"
    print "What algorithm do you want to execute?"
    print "Type 1 for Random Algorithm"
    print "Type 2 for Hillclimber for one field"
    print "Type 3 for repeated Hillclimber"
    print "Type 4 for Simulated Annealing for one field"
    print "Type 5 for repeated Simulated Annealing\n"

    algorithm = integerInput("Type: ")

    filename = "DEFAULT"
    if algorithm == 1 or algorithm == 3 or algorithm == 5:
        print "\nGive a filename of the resulting .CSV file"
        filename = str(raw_input("Filename: "))

    if algorithm == 1:
        print "\nHow many times do you want to execute the algorithm?"
        runs = 0
        while runs <= 0:
            runs = integerInput("Number of runs: ")
        print "\nRANDOM"
        randomAlgorithm(runs, filename)

    elif algorithm == 2:
        variant = 0
        while variant != 20 and variant != 40 and variant != 60:
            print "\nWhat variant do you want to climb?"
            variant = integerInput("Type 20, 40 or 60: ")
        print "\nWhat is the maximum amount of moves you want to make?"
        moves = 0
        while moves <= 0:
            moves = integerInput("Number of moves: ")
        print "\nDo you want to see a visualization?"
        visualize = raw_input("Type yes for visualization, else no visualization: ")
        print "\nHILLCLIMBER"
        hillClimber(moves, variant, visualize, optimalisatietype)

    elif algorithm == 3:
        print "\nHow many times do you want to execute the algorithm?"
        runs = 0
        while runs <= 0:
            runs = integerInput("Number of runs: ")
        print "\nREPEATED HILLCLIMBER"
        repeatHillClimber(runs, filename)

    elif algorithm == 4:
        print "\nDo you want to see a visualization?"
        visualize = raw_input("Type yes for visualization, else no visualization: ")
        print "\nSIMULATED ANNEALING"
        # variant, T, T_min, alpha, maxIterations, visualize
        simulatedAnnealing(20, 1.0, 0.0002, 0.99, 50, visualize)

    elif algorithm == 5:
        print "\nHow many times do you want to execute the algorithm?"
        runs = 0
        while runs <= 0:
            runs = integerInput("Number of runs: ")
        print "\nREPEATED SIMULATED ANNEALING"
        repeatSimulatedAnnealing(runs, filename)

    else:
        print "\n ### Choose a valid type ###"
        runProgram()

    print ""

runProgram()
