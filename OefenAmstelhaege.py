# OefenAmstelhaege.py
# Jasper Scholten
# 11157887

import numpy
import matplotlib.pyplot as plt

# 160 meter in pieces of 0,5 meter
height = 320
# 150 meter in pieces of 0,5 meter
width = 300

# print height*width
area = numpy.zeros((height,width), dtype="int32")

for x in range(40, 140):
    for y in range(40, 140):
        area[(y, x)] = 1

for x in range(40, 140):
    for y in range(160, 180):
        area[(y, x)] = 1

for x in range(180, 210):
    for y in range(60, 250):
        area[(y, x)] = 2

print area

plt.imshow(area)
#plt.gray()
plt.show()
