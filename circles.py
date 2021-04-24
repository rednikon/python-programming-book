# pg. 76, problem 1: Mathematical expressions

import math

def get_volume():
    radius = int(input("Let's calculate the volume and area of a circle. Please enter a value for the radius: "))
    volume = 4 / 3 * (math.pi * radius**3)
    area = 4 * math.pi * radius**2
    print("The circle's volume is: ", round(volume, 2), "and the circle's area is: ", round(area, 2))

get_volume()
