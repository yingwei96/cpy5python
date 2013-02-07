# Filename: q02_triangle.py
# Author: Lim Ying Wei
# Created: 20130129
# Modified: 20130129
# Description: Program to check if triangle is valid and its perimeter

# main

# promt and get numbers
number = float(input("Enter Side 1: "))
side= float(input("Enter Side 2: "))
base= float(input("Enter Side 3: "))

# find perimeter
add= number + side + base

# Check if triangle is valid
if (number + side) <= base:
    print("Invalid Triangle!")
elif (number + base) <= side:
    print("Invalid Triangle!")
elif (base + side) <= number:
    print("Invalid Triangle!")
else:
    print("Perimeter = {0:.2f}".format(add))
