from IPython.display import clear_output
from math import pi


def calc(calctype):
    if calctype == 1:
        length = float(input('What is the length of the house?\n'))
        width = float(input('What is the width of the house?\n'))
        clear_output()
        area = length * width
        print(f'The area of the house is {area}')
    else:
        diameter = float(input('What is the diameter of the circle?\n'))
        clear_output()
        circum = diameter * pi
        print(f'The circumerence is {round(circum,2)}')