# Filename: q3_sun_digits.py
# Author: Lim Ying Wei
# Created: 20130124
# Modified: 20120124
# Description: Program to get sum of digits

# main

# promt and get number
number = int(input("Enter an integer between 0 and 1000: "))

# establish invalid numbers
if number <= 0:
    print ("Number Invalid")
if number >= 1000:
    print ("Number Invalid")
else:

# establish digits in the number
    ones = number % 10
    tens = ((number % 100) - ones)/10
    hundreds = number // 100

#add digits
    add = ones + tens + hundreds

# display results
    print ("Sum of Digits= {0:.0f}".format(add))
