# Wat we nu doen is (zo goed als) continu, met komma getallen.
# Kan je in principe hogere, nauwkeurigere waarde mee vinden.
# discreet is met gehele getallen -> Wouter
# hoe meer discretiseren, hoe minder accuraat: keuze op dit gebied is
# interresant voor verslag.

distance = 1000000.0
x_coordinate = 0.0
y_coordinate = 0.0

# loop through housetypes
for i in range(3):
    # loop through houses of certain type
    for j in range(len(houses[i])):
        # loop through corner coordinates
        for k in range(4):
            if k == 0:
                if i == 0:
                    x_coordinate = houses[i]["maison{0}".format(j)][2]
                    y_coordinate = houses[i]["maison{0}".format(j)][3]
                elif i == 1:
                    x_coordinate = houses[i]["bungalow{0}".format(j)][2]
                    y_coordinate = houses[i]["bungalow{0}".format(j)][3]
                else:
                    x_coordinate = houses[i]["singlefamily{0}".format(j)][2]
                    y_coordinate = houses[i]["singlefamily{0}".format(j)][3]
            if k == 1:
                if i == 0:
                    x_coordinate = houses[i]["maison{0}".format(j)][4]
                    y_coordinate = houses[i]["maison{0}".format(j)][5]
                elif i == 1:
                    x_coordinate = houses[i]["bungalow{0}".format(j)][4]
                    y_coordinate = houses[i]["bungalow{0}".format(j)][5]
                else:
                    x_coordinate = houses[i]["singlefamily{0}".format(j)][4]
                    y_coordinate = houses[i]["singlefamily{0}".format(j)][5]
            if k == 2:
                if i == 0:
                    x_coordinate = houses[i]["maison{0}".format(j)][6]
                    y_coordinate = houses[i]["maison{0}".format(j)][7]
                elif i == 1:
                    x_coordinate = houses[i]["bungalow{0}".format(j)][6]
                    y_coordinate = houses[i]["bungalow{0}".format(j)][7]
                else:
                    x_coordinate = houses[i]["singlefamily{0}".format(j)][6]
                    y_coordinate = houses[i]["singlefamily{0}".format(j)][7]
            if k == 3:
                if i == 0:
                    x_coordinate = houses[i]["maison{0}".format(j)][8]
                    y_coordinate = houses[i]["maison{0}".format(j)][9]

                elif i == 1:
                    x_coordinate = houses[i]["bungalow{0}".format(j)][8]
                    y_coordinate = houses[i]["bungalow{0}".format(j)][9]
                else:
                    x_coordinate = houses[i]["singlefamily{0}".format(j)][8]
                    y_coordinate = houses[i]["singlefamily{0}".format(j)][9]

            coordistance = 0.0

            # valt x coordinaat binnen huis -> muur tot muur.
            if x_lu <= x_coordinate <= x_ru:
                # kan in een functie (voor later)
                if y_lu <= y_coordinate:
                    coordistance = y_coordinate - y_ld
                else:
                    coordistance = y_lu - y_coordinate
            # valt y coordinaat binnen huis -> muur tot muur.
            elif y_lu <= y_coordinate <= y_ld:
                if x_lu <= x_coordinate:
                    coordistance = x_coordinate - x_ru
                else:
                    coordistance = x_lu - x_coordinate
            #hoekgevallen
            else:
                # if, elif, else gebruiken?
                if x_coordinate < x_lu and y_coordinate < y_lu:
                    # leftup
                    coordistance = math.sqrt((y_lu - y_coordinate) ** 2 + (x_lu - x_coordinate) ** 2)
                if x_coordinate > x_ru and y_coordinate < y_ru:
                    # rightup
                    coordistance = math.sqrt((y_ru - y_coordinate) ** 2 + (x_coordinate - x_ru) ** 2)
                if x_coordinate < x_ld and y_coordinate > y_ld:
                    # leftdown
                    coordistance = math.sqrt((y_coordinate - y_ld) ** 2 + (x_ld - x_coordinate) ** 2)
                if x_coordinate > x_rd and y_coordinate > y_rd:
                    # rightdown
                    coordistance = math.sqrt((y_coordinate - y_rd) ** 2 + (x_coordinate - x_rd) ** 2)

            #print(coordistance)
            if coordistance < distance:
                distance = coordistance

# check nog voor de afstand naar de kant
# bereken voor de vier muren de afstand
# als een van deze korter is --> nieuwe kortste afstand

return round(distance, 2)
