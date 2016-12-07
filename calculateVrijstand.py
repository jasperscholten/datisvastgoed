import math

# should be 9
# houses = [-158600.0, -21.0, 0, 0, 1, 0, 0, 2, 1, 2], [-158600.0, -21.0, 10, 1, 11, 1, 10, 3, 11, 3]

#should be 9.05
#houses = [-158600.0, -21.0, 0, 0, 1, 0, 0, 2, 1, 2], [-158600.0, -21.0, 10, 3, 11, 3, 10, 4, 11, 4]

houses = [-158600.0, -21.0, 5, 5, 6, 5, 5, 6, 6, 6], [-158600.0, -21.0, 0, 10, 10, 10, 0, 20, 10, 20]

print houses

['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']

# zorg ervoor dat: a < b, c < d
def betweenCorners(a, b, c, d):
    if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
        return True
    else:
        return False

distance = 0

# huis 1: ax, ay - huis 2: bx, by
def pythagoras(ax, ay, bx, by):
    length = abs(ax - bx)
    width = abs(ay - by)

    return math.sqrt(length**2 + width**2)

# huis 1 y_lu >= huis 2 y_ld
# boven
if houses[0][3] >= houses[1][7]:
# huis 2 x_lu en/of x_ru tussen huis 1 x_lu en x_ru
    if betweenCorners(houses[0][2], houses[0][4], houses[1][2], houses[1][4]):
        distance = houses[0][3] - houses[1][7]
    else:
        # 1_lu, 2_rd
        print "pythagoras boven"
        distance = min(pythagoras(houses[0][2], houses[0][3], houses[1][8], houses[1][9]), pythagoras(houses[0][4], houses[0][5], houses[1][6], houses[1][7]))
# huis 1 y_ld <= huis 2 y_lu
# onder
elif houses[0][7] <= houses[1][3]:
    if betweenCorners(houses[0][2], houses[0][4], houses[1][2], houses[1][4]):
        distance = houses[1][3] - houses[0][7]
    else:
        print "pythagoras onder"
        distance = min(pythagoras(houses[0][6], houses[0][7], houses[1][4], houses[1][5]), pythagoras(houses[0][8], houses[0][9], houses[1][2], houses[1][3]))
else:
    # left
    if houses[0][2] >= houses[1][4]:
        distance = houses[0][2] - houses[1][4]
    # right
    else:
        distance = houses[1][2] - houses[0][4]

print distance
