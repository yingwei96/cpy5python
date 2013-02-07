# Filename: q04_determine_leap_year.py
# Author: Lim Ying Wei
# Created: 20130129
# Modified: 20130129
# Description: Program to determine if year is a leap year

# main

#Prompt for year
year = int(input("Enter Year: "))

# evaluate if year is leap year
if year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
elif year % 400 == 0:
    print("Leap Year")
else:
    print("Non-Leap Year")
