import math
import collections

#houses = ({'maison8': [-158600.0, -21.0, 257, 156, 279, 156, 257, 177, 279, 177], 'maison0': [-158600.0, -21.0, 141, 25, 163, 25, 141, 46, 163, 46], 'maison1': [-158600.0, -21.0, 134, 89, 156, 89, 134, 110, 156, 110], 'maison2': [-158600.0, -21.0, 155, 203, 177, 203, 155, 224, 177, 224], 'maison3': [-158600.0, -21.0, 266, 73, 288, 73, 266, 94, 288, 94]})

houses = ({'maison8': [829600.0, 6.0, 116, 223, 138, 223, 116, 244, 138, 244], 'maison0': [829600.0, 6.0, 78, 220, 100, 220, 78, 241, 100, 241], 'maison1': [847900.0, 6.5, 218, 103, 240, 103, 218, 124, 240, 124], 'maison2': [884500.0, 7.5, 187, 276, 209, 276, 187, 297, 209, 297], 'maison3': [866200.0, 7.0, 228, 255, 250, 255, 228, 276, 250, 276], 'maison4': [866200.0, 7.0, 147, 276, 169, 276, 147, 297, 169, 297], 'maison5': [868801.08, 7.0710678118654755, 52, 71, 74, 71, 52, 92, 74, 92], 'maison6': [829600.0, 6.0, 76, 257, 98, 257, 76, 278, 98, 278], 'maison7': [884500.0, 7.5, 252, 133, 274, 133, 252, 154, 274, 154]}, {'bungalow8': [521070.53, 7.648529270389178, 272, 60, 292, 60, 272, 75, 292, 75], 'bungalow9': [478800.0, 5.0, 229, 207, 249, 207, 229, 222, 249, 222], 'bungalow0': [494760.0, 6.0, 272, 170, 292, 170, 272, 185, 292, 185], 'bungalow1': [446880.0, 3.0, 128, 6, 148, 6, 128, 21, 148, 21], 'bungalow2': [446880.0, 3.0, 100, 92, 120, 92, 100, 107, 120, 107], 'bungalow3': [454860.0, 3.5, 127, 94, 147, 94, 127, 109, 147, 109], 'bungalow4': [462840.0, 4.0, 20, 251, 40, 251, 20, 266, 40, 266], 'bungalow5': [494760.0, 6.0, 12, 187, 32, 187, 12, 202, 32, 202], 'bungalow6': [446880.0, 3.0, 152, 48, 172, 48, 152, 63, 172, 63], 'bungalow7': [447540.44, 3.0413812651491097, 237, 42, 257, 42, 237, 57, 257, 57], 'bungalow12': [478800.0, 5.0, 181, 96, 201, 96, 181, 111, 201, 111], 'bungalow13': [498989.11, 6.264982043070834, 233, 171, 253, 171, 233, 186, 253, 186], 'bungalow10': [471261.97, 4.527692569068709, 9, 292, 29, 292, 9, 307, 29, 307], 'bungalow11': [446880.0, 3.0, 170, 246, 190, 246, 170, 261, 190, 261], 'bungalow14': [462840.0, 4.0, 17, 7, 37, 7, 17, 22, 37, 22]}, {'singlefamily33': [302100.0, 2.0, 28, 227, 44, 227, 28, 243, 44, 243], 'singlefamily32': [323475.0, 4.5, 111, 256, 127, 256, 111, 272, 127, 272], 'singlefamily31': [310650.0, 3.0, 48, 253, 64, 253, 48, 269, 64, 269], 'singlefamily30': [306375.0, 2.5, 195, 218, 211, 218, 195, 234, 211, 234], 'singlefamily35': ['value', 'vrijstand', 155, 91, 171, 91, 155, 107, 171, 107], 'singlefamily34': [310650.0, 3.0, 38, 275, 54, 275, 38, 291, 54, 291], 'singlefamily11': [314925.0, 3.5, 7, 30, 23, 30, 7, 46, 23, 46], 'singlefamily10': [336300.0, 6.0, 21, 159, 37, 159, 21, 175, 37, 175], 'singlefamily13': [323475.0, 4.5, 117, 281, 133, 281, 117, 297, 133, 297], 'singlefamily12': [311003.81, 3.0413812651491097, 258, 20, 274, 20, 258, 36, 274, 36], 'singlefamily15': [302100.0, 2.0, 21, 92, 37, 92, 21, 108, 37, 108], 'singlefamily14': [302100.0, 2.0, 8, 223, 24, 223, 8, 239, 24, 239], 'singlefamily17': [310650.0, 3.0, 99, 70, 115, 70, 99, 86, 115, 86], 'singlefamily16': [306375.0, 2.5, 174, 224, 190, 224, 174, 240, 190, 240], 'singlefamily19': [302100.0, 2.0, 11, 112, 27, 112, 11, 128, 27, 128], 'singlefamily18': [323475.0, 4.5, 65, 33, 81, 33, 65, 49, 81, 49], 'singlefamily9': [340575.0, 6.5, 273, 285, 289, 285, 273, 301, 289, 301], 'singlefamily8': [319200.0, 4.0, 274, 256, 290, 256, 274, 272, 290, 272], 'singlefamily1': [306375.0, 2.5, 83, 5, 99, 5, 83, 21, 99, 21], 'singlefamily0': [319200.0, 4.0, 45, 5, 61, 5, 45, 21, 61, 21], 'singlefamily3': [319200.0, 4.0, 45, 299, 61, 299, 45, 315, 61, 315], 'singlefamily2': [304118.38, 2.23606797749979, 22, 53, 38, 53, 22, 69, 38, 69], 'singlefamily5': [327750.0, 5.0, 259, 197, 275, 197, 259, 213, 275, 213], 'singlefamily4': [361950.0, 9.0, 269, 99, 285, 99, 269, 115, 285, 115], 'singlefamily7': [304118.38, 2.23606797749979, 40, 33, 56, 33, 40, 49, 56, 49], 'singlefamily6': [310650.0, 3.0, 154, 69, 170, 69, 154, 85, 170, 85], 'singlefamily28': [340575.0, 6.5, 161, 14, 177, 14, 161, 30, 177, 30], 'singlefamily29': [323475.0, 4.5, 127, 54, 143, 54, 127, 70, 143, 70], 'singlefamily24': [319200.0, 4.0, 207, 67, 223, 67, 207, 83, 223, 83], 'singlefamily25': [306375.0, 2.5, 190, 13, 206, 13, 190, 29, 206, 29], 'singlefamily26': [310650.0, 3.0, 50, 229, 66, 229, 50, 245, 66, 245], 'singlefamily27': [319200.0, 4.0, 231, 74, 247, 74, 231, 90, 247, 90], 'singlefamily20': [310650.0, 3.0, 198, 240, 214, 240, 198, 256, 214, 256], 'singlefamily21': [306375.0, 2.5, 211, 15, 227, 15, 211, 31, 227, 31], 'singlefamily22': [323475.0, 4.5, 237, 295, 253, 295, 237, 311, 253, 311], 'singlefamily23': [319200.0, 4.0, 268, 232, 284, 232, 268, 248, 284, 248]}, {'water1': [187, 33, 230, 33, 187, 54, 230, 54], 'water0': [37, 126, 222, 126, 37, 218, 222, 218], 'water2': [99, 31, 146, 31, 99, 54, 146, 54]})

selection = {k: v for k, v in houses[0].items() if v[2] > 250}
selection.update({k: v for k, v in houses[1].items() if v[2] > 250})
selection.update({k: v for k, v in houses[2].items() if v[2] > 250})
print selection

#print(houses[0]["maison{0}".format(j)])



# meegeven: houses, type, type_string, firstIndex, i, step

# move 1m to right
    # change coordinates
    housesCopy = deepcopy(houses)

    housesCopy[type][type_string.format(i)][firstIndex] = houses_rght[type][type_string.format(i)][firstIndex] + step
    houses_rght[type][type_string.format(i)][firstIndex + 2] = houses_rght[type][type_string.format(i)][firstIndex + 2] + step
    houses_rght[type][type_string.format(i)][firstIndex + 4] = houses_rght[type][type_string.format(i)][firstIndex + 4] + step
    houses_rght[type][type_string.format(i)][firstIndex + 6] = houses_rght[type][type_string.format(i)][firstIndex + 6] + step

    housesCopy = self.getFilteredVrijstand(housesCopy, type_string, i, type)
    housesCopy[type][type_string.format(i)][0] = self.calculateValue(type, housesCopy[type][type_string.format(i)][1])

    return housesCopy


    fieldvalue_rght = self.totalValue(houses_rght)

    # pick highest value
    newfieldvalue = max([fieldvalue_rght, fieldvalue_lft, fieldvalue_up, fieldvalue_dwn])



# meegeven: house (bv. houses_rght)

if newfieldvalue == fieldvalue_rght:

    for y in range(house[type][type_string.format(i)][3], house[type][type_string.format(i)][7]):
        self.area[(y, house[type][type_string.format(i)][4] - 1)] = 0
        self.area[(y, house[type][type_string.format(i)][4] - 2)] = 0
        self.area[(y, house[type][type_string.format(i)][2])] = type + 1
        self.area[(y, house[type][type_string.format(i)][2] - 1)] = type + 1

    return house

elif newfieldvalue == fieldvalue_lft:
    for y in range(houses_lft[type][type_string.format(i)][3], houses_lft[type][type_string.format(i)][7]):
        self.area[(y, houses_lft[type][type_string.format(i)][2] + 1)] = 0
        self.area[(y, houses_lft[type][type_string.format(i)][2] + 2)] = 0
        self.area[(y, houses_lft[type][type_string.format(i)][4])] = type + 1
        self.area[(y, houses_lft[type][type_string.format(i)][4] + 1)] = type + 1

    return houses_lft

elif newfieldvalue == fieldvalue_dwn:
    for x in range(houses_dwn[type][type_string.format(i)][2], houses_dwn[type][type_string.format(i)][4]):
        self.area[(houses_dwn[type][type_string.format(i)][7] - 1, x)] = 0
        self.area[(houses_dwn[type][type_string.format(i)][7] - 2, x)] = 0
        self.area[(houses_dwn[type][type_string.format(i)][3], x)] = type + 1
        self.area[(houses_dwn[type][type_string.format(i)][3] - 1, x)] = type + 1
    return houses_dwn

else:
    for x in range(houses_up[type][type_string.format(i)][2], houses_up[type][type_string.format(i)][4]):
        self.area[(houses_up[type][type_string.format(i)][3] + 1, x)] = 0
        self.area[(houses_up[type][type_string.format(i)][3] + 2, x)] = 0
        self.area[(houses_up[type][type_string.format(i)][7], x)] = type + 1
        self.area[(houses_up[type][type_string.format(i)][7] + 1, x)] = type + 1
    return houses_up



houses_up = deepcopy(houses)

houses_up[type][type_string.format(i)][3] = houses_up[type][type_string.format(i)][3] - 2
houses_up[type][type_string.format(i)][5] = houses_up[type][type_string.format(i)][5] - 2
houses_up[type][type_string.format(i)][7] = houses_up[type][type_string.format(i)][7] - 2
houses_up[type][type_string.format(i)][9] = houses_up[type][type_string.format(i)][9] - 2

#calcualte vrijstand and value
# currentHouse_up[1] = area.getFilteredVrijstand(currentHouse_up, houses)
houses_up = self.getFilteredVrijstand(houses_up, type_string, i, type)
# currentHouse_up[0] = area.calculateValue(type, currentHouse_up[1])
houses_up[type][type_string.format(i)][0] = self.calculateValue(type, houses_up[type][type_string.format(i)][1])
fieldvalue_up = self.totalValue(houses_up)
