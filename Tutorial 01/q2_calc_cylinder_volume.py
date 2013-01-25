# Filename: q2_calc_cylinder_volume.py
# Author: Lim Ying Wei
# Created: 20130122
# Modified: 20120122
# Description: Program to get volume of cylinder

# main

# promt and get radius of base
radius = float(input("Enter Radius in cm: "))

# prompt and get height
length = float(input("Enter Length in cm: "))

# calculate volume of cylinder
from math import pi
vol = (pi) * radius*radius * length

# display results
print ("Volume= {0:.1f}".format(vol))
