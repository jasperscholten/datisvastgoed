import math

# should be 9
# houses = [-158600.0, -21.0, 0, 0, 1, 0, 0, 2, 1, 2], [-158600.0, -21.0, 10, 1, 11, 1, 10, 3, 11, 3]

#should be 9.05
#houses = [-158600.0, -21.0, 0, 0, 1, 0, 0, 2, 1, 2], [-158600.0, -21.0, 10, 3, 11, 3, 10, 4, 11, 4]

houses = [379050.0, 13.0, 220, 252, 236, 252, 220, 268, 236, 268], [794660.21, 6.082762530298219, 190, 229, 212, 229, 190, 250, 212, 250]



['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

def betweenCorners(a, b, c, d):
    if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
        return True
    else:
        return False

# huis 1: ax, ay - huis 2: bx, by
def pythagoras(ax, ay, bx, by):
    length = abs(ax - bx)
    width = abs(ay - by)

    return math.sqrt(length**2 + width**2)

def calculateVrijstand(houses):
    # boven
    # huis 1 y_lu >= huis 2 y_ld
    if houses[0][3] >= houses[1][7]:
    # huis 2 x_lu en/of x_ru tussen huis 1 x_lu en x_ru
        if betweenCorners(houses[0][2], houses[0][4], houses[1][2], houses[1][4]):
            distance = houses[0][3] - houses[1][7]
            #print "huis boven tussen:", distance
        else:
            # 1_lu, 2_rd
            distance = min(pythagoras(houses[0][2], houses[0][3], houses[1][8], houses[1][9]), pythagoras(houses[0][4], houses[0][5], houses[1][6], houses[1][7]))
            #print "huis boven hoeken:", distance
    # onder
    # huis 1 y_ld <= huis 2 y_lu
    elif houses[0][7] <= houses[1][3]:
        if betweenCorners(houses[0][2], houses[0][4], houses[1][2], houses[1][4]):
            distance = houses[1][3] - houses[0][7]
            #print "huis onder tussen:", distance
        else:
            distance = min(pythagoras(houses[0][6], houses[0][7], houses[1][4], houses[1][5]), pythagoras(houses[0][8], houses[0][9], houses[1][2], houses[1][3]))
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

print calculateVrijstand(houses)
