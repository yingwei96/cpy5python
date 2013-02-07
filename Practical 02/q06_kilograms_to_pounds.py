# Filename: q06_kilograms_to_pounds.py
# Author: Lim Ying Wei
# Created: 20130201
# Modified: 20130201
# Description: Program to list kilograms to pounds

print("{0:<10} {1:>10}".format ("Kilograms","Pounds"))

i = 1
while (i <= 10):
    print ("{0:<10} {1:>10.1f}".format (int(i), float(i*2.2)))
    i = i + 1
