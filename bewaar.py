x_search = x_pos - 14
    y_search = y_pos - 14
    counter = 0
    while True:
        for j in range(x_search - 2 * counter, x_search + 2 * 12 + 22 + 2 + 2 * counter):
            if (self.area[(j, y_search - 2 * counter)] != 0 and self.area[(j, y_search - 2 * counter)] != 4) or (j > width or j < 0):
                return counter
        for k in range(y_search - 2 * counter, y_search + 2 * 12 + 21 + 2 + 2 * counter):
            if self.area[(x_search + 2 * 12 + 22 + 2 + 2 * counter, k)] != 0 and self.area[(x_search + 2 * 12 + 22 + 2 + 2 * counter, k)] != 4 or (k > height or k < 0):
                return counter
        for l in range(x_search - 2 * counter, x_search + 2 * 12 + 22 + 2 + 2 * counter):
            if self.area[(l, y_search + 2 * 12 + 21 + 2 + 2 * counter)] != 0 and self.area[(l, y_search + 2 * 12 + 21 + 2 + 2 * counter)] != 4 or (l > width or l < 0):
                return counter
        for m in range(y_search - 2 * counter, y_search + 2 * 12 + 21 + 2 + 2 * counter):
            if self.area[(x_search - 2 * counter, m)] != 0 and self.area[(x_search - 2 * counter, m)] != 4 or (k > height or k < 0):
                return counter
        counter += 1

        '''houses[3]["water{0}".format(counter - 1)][0] = x_pos
        houses[3]["water{0}".format(counter - 1)][1] = y_pos
        houses[3]["water{0}".format(counter - 1)][2] = x_pos + waterLength
        houses[3]["water{0}".format(counter - 1)][3] = y_pos
        houses[3]["water{0}".format(counter - 1)][4] = x_pos
        houses[3]["water{0}".format(counter - 1)][5] = y_pos + waterWidth
        houses[3]["water{0}".format(counter - 1)][6] = x_pos + waterLength
        houses[3]["water{0}".format(counter - 1)][7] = y_pos + waterWidth

        houses[0]["maison{0}".format(counter)][2] = x_pos
        houses[0]["maison{0}".format(counter)][3] = y_pos
        houses[0]["maison{0}".format(counter)][4] = x_pos + 22
        houses[0]["maison{0}".format(counter)][5] = y_pos
        houses[0]["maison{0}".format(counter)][6] = x_pos
        houses[0]["maison{0}".format(counter)][7] = y_pos + 21
        houses[0]["maison{0}".format(counter)][8] = x_pos + 22
        houses[0]["maison{0}".format(counter)][9] = y_pos + 21

        houses[1]["bungalow{0}".format(counter)][2] = x_pos
        houses[1]["bungalow{0}".format(counter)][3] = y_pos
        houses[1]["bungalow{0}".format(counter)][4] = x_pos + 20
        houses[1]["bungalow{0}".format(counter)][5] = y_pos
        houses[1]["bungalow{0}".format(counter)][6] = x_pos
        houses[1]["bungalow{0}".format(counter)][7] = y_pos + 15
        houses[1]["bungalow{0}".format(counter)][8] = x_pos + 20
        houses[1]["bungalow{0}".format(counter)][9] = y_pos + 15

        houses[2]["singlefamily{0}".format(counter)][2] = x_pos
        houses[2]["singlefamily{0}".format(counter)][3] = y_pos
        houses[2]["singlefamily{0}".format(counter)][4] = x_pos + 16
        houses[2]["singlefamily{0}".format(counter)][5] = y_pos
        houses[2]["singlefamily{0}".format(counter)][6] = x_pos
        houses[2]["singlefamily{0}".format(counter)][7] = y_pos + 16
        houses[2]["singlefamily{0}".format(counter)][8] = x_pos + 16
        houses[2]["singlefamily{0}".format(counter)][9] = y_pos + 16'''






        '''
          Moet ingekort worden.
          '''
          def moveHouse(self, houses, type_string, i, fieldvalue, type):
          # currentHouse = ['value', 'vrijstand', 'x_lu', 'y_lu', 'x_ru', 'y_ru', 'x_ld', 'y_ld', 'x_rd', 'y_rd']
          # move 1m up
              # change coordinates

              #print i
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

          # move 1m down
              # change coordinates
              houses_dwn = deepcopy(houses)

              houses_dwn[type][type_string.format(i)][3] = houses_dwn[type][type_string.format(i)][3] + 2
              houses_dwn[type][type_string.format(i)][5] = houses_dwn[type][type_string.format(i)][5] + 2
              houses_dwn[type][type_string.format(i)][7] = houses_dwn[type][type_string.format(i)][7] + 2
              houses_dwn[type][type_string.format(i)][9] = houses_dwn[type][type_string.format(i)][9] + 2

              houses_dwn = self.getFilteredVrijstand(houses_dwn, type_string, i, type)
              houses_dwn[type][type_string.format(i)][0] = self.calculateValue(type, houses_dwn[type][type_string.format(i)][1])

              fieldvalue_dwn = self.totalValue(houses_dwn)

          # move 1m to left
              # change coordinates
              houses_lft = deepcopy(houses)

              houses_lft[type][type_string.format(i)][2] = houses_lft[type][type_string.format(i)][2] - 2
              houses_lft[type][type_string.format(i)][4] = houses_lft[type][type_string.format(i)][4] - 2
              houses_lft[type][type_string.format(i)][6] = houses_lft[type][type_string.format(i)][6] - 2
              houses_lft[type][type_string.format(i)][8] = houses_lft[type][type_string.format(i)][8] - 2

              houses_lft = self.getFilteredVrijstand(houses_lft, type_string, i, type)
              houses_lft[type][type_string.format(i)][0] = self.calculateValue(type, houses_lft[type][type_string.format(i)][1])

              fieldvalue_lft = self.totalValue(houses_lft)

          # move 1m to right
              # change coordinates
              houses_rght = deepcopy(houses)

              houses_rght[type][type_string.format(i)][2] = houses_rght[type][type_string.format(i)][2] + 2
              houses_rght[type][type_string.format(i)][4] = houses_rght[type][type_string.format(i)][4] + 2
              houses_rght[type][type_string.format(i)][6] = houses_rght[type][type_string.format(i)][6] + 2
              houses_rght[type][type_string.format(i)][8] = houses_rght[type][type_string.format(i)][8] + 2

              houses_rght = self.getFilteredVrijstand(houses_rght, type_string, i, type)
              houses_rght[type][type_string.format(i)][0] = self.calculateValue(type, houses_rght[type][type_string.format(i)][1])

              fieldvalue_rght = self.totalValue(houses_rght)

              # pick highest value
              newfieldvalue = max([fieldvalue_rght, fieldvalue_lft, fieldvalue_up, fieldvalue_dwn])


              if newfieldvalue > fieldvalue:

                  if newfieldvalue == fieldvalue_rght:
                      for y in range(houses_rght[type][type_string.format(i)][3], houses_rght[type][type_string.format(i)][7]):
                          self.area[(y, houses_rght[type][type_string.format(i)][4] - 1)] = 0
                          self.area[(y, houses_rght[type][type_string.format(i)][4] - 2)] = 0
                          self.area[(y, houses_rght[type][type_string.format(i)][2])] = type + 1
                          self.area[(y, houses_rght[type][type_string.format(i)][2] - 1)] = type + 1

                      return houses_rght

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
              else:
                  #print self.totalValue(houses)
                  return houses

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



def getFilteredVrijstand(self, houses, type_string, i, type):

      # Hoe weten welke variant we bekijken?
      # 20 huizen: 100 ruimte - 40 huizen: 75 - 60 huizen: 50

      housesCopy = deepcopy(houses)

      x_lu = housesCopy[type][type_string.format(i)][2] - 100
      x_ru = housesCopy[type][type_string.format(i)][4] + 100
      y_lu = housesCopy[type][type_string.format(i)][3] - 100
      y_ld = housesCopy[type][type_string.format(i)][7] + 100

      selection = {}
      #http://stackoverflow.com/questions/2844516/how-to-filter-a-dictionary-according-to-an-arbitrary-condition-function
      selection1 = {k: v for k, v in housesCopy[0].items() if x_lu < (v[2] or v[4]) < x_ru or y_lu < (v[3] or v[7]) < y_ld}
      selection2 = {k: v for k, v in housesCopy[1].items() if x_lu < (v[2] or v[4]) < x_ru or y_lu < (v[3] or v[7]) < y_ld}
      selection3 = {k: v for k, v in housesCopy[2].items() if x_lu < (v[2] or v[4]) < x_ru or y_lu < (v[3] or v[7]) < y_ld}

      selection.update(selection1)
      selection.update(selection2)
      selection.update(selection3)

      vrijstand = 1000000

      currentHouse = housesCopy[type][type_string.format(i)]

      for house in selection:
          twoHouses = currentHouse, selection[house]

          currentVrijstand = self.calculateVrijstand(twoHouses)/2.0

          if 0 <= currentVrijstand < vrijstand:
              vrijstand = currentVrijstand

      distanceToWall = min((self.width - currentHouse[8]), (self.height - currentHouse[9]), currentHouse[2], currentHouse[3])
      if distanceToWall/2.0 < vrijstand:
          vrijstand = distanceToWall/2.0



      housesCopy[type][type_string.format(i)][1] = vrijstand

      for house in selection:
          if housesCopy == "invalid move":
              return "invalid move"
          housesCopy = self.getFilteredVrijstandSelection(housesCopy, house)

      return housesCopy

  def getFilteredVrijstandSelection(self, houses, housename):
      for i in range(3):
          if housename in houses[i]:
              currentHouse = houses[i][housename]

              x_lu = currentHouse[2] - 100
              x_ru = currentHouse[4] + 100
              y_lu = currentHouse[3] - 100
              y_ld = currentHouse[7] + 100

              selection = {}
              #http://stackoverflow.com/questions/2844516/how-to-filter-a-dictionary-according-to-an-arbitrary-condition-function
              selection1 = {k: v for k, v in houses[0].items() if x_lu < (v[2] or v[4]) < x_ru or y_lu < (v[3] or v[7]) < y_ld}
              selection2 = {k: v for k, v in houses[1].items() if x_lu < (v[2] or v[4]) < x_ru or y_lu < (v[3] or v[7]) < y_ld}
              selection3 = {k: v for k, v in houses[2].items() if x_lu < (v[2] or v[4]) < x_ru or y_lu < (v[3] or v[7]) < y_ld}

              selection.update(selection1)
              selection.update(selection2)
              selection.update(selection3)

              vrijstand = 1000000

              for house in selection:
                  twoHouses = currentHouse, selection[house]

                  currentVrijstand = self.calculateVrijstand(twoHouses)/2.0

                  if 0 <= currentVrijstand < vrijstand:
                      vrijstand = currentVrijstand

              distanceToWall = min((self.width - currentHouse[8]), (self.height - currentHouse[9]), currentHouse[2], currentHouse[3])
              if distanceToWall/2.0 < vrijstand:
                  vrijstand = distanceToWall/2.0

              if "maison" in housename and vrijstand < 6:
                  return "invalid move"
              if "bungalow" in housename and vrijstand < 3:
                  return "invalid move"
              if "singlefamily" in housename and vrijstand < 2:
                  return "invalid move"

              for i in range(2):
                  if housename in houses[i]:
                      houses[i][housename.format(i)][1] = vrijstand

              return houses
