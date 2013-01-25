# Filename: q6_find_ascii_char.py
# Author: Lim Ying Wei
# Created: 20130124
# Modified: 20120124
# Description: Program to get character from ASCII code

# main

# promt and get code
code = int(input("Enter Code: "))

#invalid codes
if code < 0:
    print ("Invalid Code")
if code > 127:
    print ("Invalid Code")
else:
    
# convert code to character
    character = chr(code)

# display results
    print ("Character= {0:}".format(character))
