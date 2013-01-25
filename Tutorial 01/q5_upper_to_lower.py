# Filename: q5_upper_to_lower.py
# Author: Lim Ying Wei
# Created: 20130124
# Modified: 20120124
# Description: Program to convert upper case
# to lower case


# main

# promt and get upper case letter
letter = (input("Enter Upper Case Letter: "))

# convert upper case to lower case
lowletter = chr(ord(letter) + 32)

# display results
print ("Lower Case Letter= {0:}".format(lowletter))
