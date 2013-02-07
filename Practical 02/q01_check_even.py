# Filename: q01_check_even.py
# Author: Lim Ying Wei
# Created: 20130129
# Modified: 20130129
# Description: Program to check if number is even

# main

# promt and get number
number = int(input("Enter Number: "))

# Check if number is even
if number % 2 == 1:
    print(format(number) + " is Odd")
else:
    print(format(number) + " is Even")
