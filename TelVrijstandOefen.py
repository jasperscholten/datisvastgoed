def createVariables(mais, bung, egws):
    maison = dict()
    bungalow = dict()
    singlefam = dict()

    for i in range(mais):
        maison["maison{0}".format(i)] = ['value', 'vrijstand', 'x_start', 'y_start']

    for i in range(bung):
        bungalow["bungalow{0}".format(i)] = ['value', 'vrijstand', 'x_start', 'y_start']

    for i in range(egws):
        singlefam["singlefamily{0}".format(i)] = ['value', 'vrijstand', 'x_start', 'y_start']

    return maison, bungalow, singlefam

houses = createVariables(2, 3, 4)
print(houses)
print(houses[0]['maison0'][0])
houses[0]['maison0'][0] = 1
print(houses)
print(houses[0]['maison0'][0])

"""
Er worden nu drie dictionaries gevormd (1 per woningtype), waarbij in iedere
dictionary een array wordt aangemaakt die de waarde van de woning en de
vrijstand van een woning representeert.

({'maison0': [0, 0], 'maison1': [0, 0]}, {'bungalow0': [0, 0],
    'bungalow1': [0, 0], 'bungalow2': [0, 0]}, {'singlefamily1': [0, 0],
    'singlefamily0': [0, 0], 'singlefamily3': [0, 0], 'singlefamily2': [0, 0]})
"""
