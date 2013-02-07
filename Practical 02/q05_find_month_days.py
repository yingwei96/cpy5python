# Filename: q05_find_month_days.py 
# Author: Lim Ying Wei
# Created: 20130129
# Modified: 20130129
# Description: Program to find number of days in a month

# Main

#Prompt for month and year
year = int(input("Enter Year: "))
month = int(input("Enter Month (eg. June = 6): "))

#Calculate days in month
if month == 1:
    print("January " + format(year) + " has 31 days")
elif month == 3:
    print("March " + format(year) + " has 31 days")
elif month == 4:
    print("April " + format(year) + " has 30 days")
elif month == 5:
    print("May " + format(year) + " has 31 days")
elif month == 6:
    print("June " + format(year) + " has 30 days")
elif month == 7:
    print("July " + format(year) + " has 31 days")
elif month == 8:
    print("August " + format(year) + " has 31 days")
elif month == 9:
    print("September " + format(year) + " has 30 days")
elif month == 10:
    print("October " + format(year) + " has 31 days")
elif month == 11:
    print("November " + format(year) + " has 30 days")
elif month == 12:
    print("December " + format(year) + " has 31 days")
elif month == 2 and year % 4 == 0 and year % 100 != 0:
    print("February " + format(year) + " has 29 days")
elif month == 2 and year % 400 == 0:
    print("February " + format(year) + " has 29 days")
elif month == 2 and year % 4 !=0:
    print("February " + format(year) + " has 28 days")
else:
    print("Invalid")
