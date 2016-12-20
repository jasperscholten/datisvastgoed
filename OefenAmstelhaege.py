# OefenAmstelhaege.py
# Jasper Scholten
# 11157887

water = [0, 0, 10, 10, 30, 10, 10, 20, 30, 20]

currentHouse = [0, 0, 1, 2, 20, 2, 1, 22, 20, 22]

def betweenCorners(a, b, c, d):
    if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
        return True
    else:
        return False

if betweenCorners(water[2], water[4], currentHouse[2], currentHouse[4]):
    if betweenCorners(water[3], water[7], currentHouse[3], currentHouse[7]):
        print "jaa"
    else:
        print "nee2"
else:
    print "nee"
