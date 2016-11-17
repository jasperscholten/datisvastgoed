def createVariables(mais, bung, egws):
    maison = dict()
    bungalow = dict()
    singlefam = dict()

    for i in range(mais):
        maison["maison{0}".format(i)] = [0,0]

    for i in range(bung):
        bungalow["bungalow{0}".format(i)] = [0,0]

    for i in range(egws):
        singlefam["bungalow{0}".format(i)] = [0,0]

    return maison, bungalow, singlefam

houses = createVariables(2, 3, 4)
print(houses)
print(houses[0]['maison0'][0])
houses[0]['maison0'][0] = 1
print(houses)
print(houses[0]['maison0'][0])

"""
Er worden nu drie dictionaries gevormd (1 per woningtype), waarbij in iedere
dictionary een array wordt aangemaakt die de .
"""
