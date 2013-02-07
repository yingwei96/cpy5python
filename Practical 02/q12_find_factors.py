# Filename: q12_find_factors.py
# Author: Lim Ying Wei
# Created: 20130203
# Modified: 20130203
# Description: Program to find factors of integers

number = int(input("Enter Integer: "))
a = 2

while (number / a >= 1):
    if (number % a == 0):
        print(a)
        number = number/a
        
    else:
        a = a + 1
