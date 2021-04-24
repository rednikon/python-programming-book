#!/usr/bin/env python3

'''
page 76, problem 2: write a program that calculates the cost per square inch
of a circular pizza, given its diameter and price. 
'''

import math

def get_area():
    diameter = int(input("What size is your pizza? "))
    price = float(input("How much is your pizza? "))

    area = math.pi * (.5 * diameter)**2
    
    price_per = price / area
    
    print("Your pizza costs $", round(price_per, 2), " per square inch.")
    
get_area()