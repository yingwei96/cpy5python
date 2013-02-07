# Filename: q10_find_largest.py
# Author: Lim Ying Wei
# Created: 20130203
# Modified: 20130203
# Description: Program to find largest integer such that n3 is less than 12,000

i = 0

while((i*i*i) < 12000):
    i = i + 1
print (int(i - 1))
