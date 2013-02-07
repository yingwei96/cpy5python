# Filename: q07_miles_to_kilometres.py
# Author: Lim Ying Wei
# Created: 20130203
# Modified: 20130203
# Description: Program to list miles to kilometres

print("{0:<10} {1:>10} {1:<10} {0:>10}".format ("Miles","Kilometers",))

i = 1
e = 20
while (i <= 10 and 20 <= e <= 65):
    print ("{0:<10} {1:<10.3f} {2:<10} {3:>10.3f}".format (int(i), float(i*1.609), int(e), float(e/1.609)))
    i = i + 1
    e = e + 5
