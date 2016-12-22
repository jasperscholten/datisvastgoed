import numpy
import random
import math
import time
import matplotlib.pyplot as plt
from copy import deepcopy
import csv
import sys

dictionary = ({'maison0': [628300.0, 6.5, 223, 179, 245, 179, 223, 200, 245, 200], 'maison1': [610000.0, 6.0, 231, 141, 253, 141, 231, 162, 253, 162], 'maison2': [610000.0, 6.0, 201, 101, 223, 101, 201, 122, 223, 122]}, {'bungalow0': [406980.0, 3.5, 273, 175, 293, 175, 273, 190, 293, 190], 'bungalow1': [399000.0, 3.0, 67, 156, 87, 156, 67, 171, 87, 171], 'bungalow2': [406980.0, 3.5, 59, 269, 79, 269, 59, 284, 79, 284], 'bungalow3': [399000.0, 3.0, 156, 125, 176, 125, 156, 140, 176, 140], 'bungalow4': [406980.0, 3.5, 222, 294, 242, 294, 222, 309, 242, 309]}, {'singlefamily9': [297825.0, 3.5, 58, 291, 74, 291, 58, 307, 74, 307], 'singlefamily8': [285000.0, 2.0, 30, 244, 46, 244, 30, 260, 46, 260], 'singlefamily1': [319200.0, 6.0, 235, 113, 251, 113, 235, 129, 251, 129], 'singlefamily0': [289275.0, 2.5, 249, 299, 265, 299, 249, 315, 265, 315], 'singlefamily3': [289275.0, 2.5, 76, 110, 92, 110, 76, 126, 92, 126], 'singlefamily2': [289275.0, 2.5, 55, 124, 71, 124, 55, 140, 71, 140], 'singlefamily5': [285000.0, 2.0, 50, 236, 66, 236, 50, 252, 66, 252], 'singlefamily4': [323475.0, 6.5, 194, 180, 210, 180, 194, 196, 210, 196], 'singlefamily7': [293550.0, 3.0, 150, 146, 166, 146, 150, 162, 166, 162], 'singlefamily6': [289275.0, 2.5, 9, 249, 25, 249, 9, 265, 25, 265], 'singlefamily11': [289275.0, 2.5, 45, 145, 61, 145, 45, 161, 61, 161], 'singlefamily10': [285000.0, 2.0, 243, 4, 259, 4, 243, 20, 259, 20]}, {'water1': ['value', 'vrijstand', 13, 24, 187, 24, 13, 82, 187, 82], 'water0': ['value', 'vrijstand', 84, 227, 250, 227, 84, 282, 250, 282]})
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
        Build a house or water on the given location
        """
        # change values in range
        for x in range(x_start - 1, x_end):
            for y in range(y_start - 1, y_end):
                self.area[(y, x)] = type

def createBestField(houses):
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
createBestField(dictionary)
