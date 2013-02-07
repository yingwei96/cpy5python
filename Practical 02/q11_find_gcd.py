# Filename: q11_find_gcd.py
# Author: Lim Ying Wei
# Created: 20130203
# Modified: 20130203
# Description: Program to find greatest dvisor

first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))

if first < second:
    smaller = int(first)
    larger = int(second)
else:
    smaller = int(second)
    larger = int(first)

if larger % smaller == 0:
    print("Greatest Common Divisor is: " + str(smaller))
    
else:
    smaller = smaller - 1
    while(larger % smaller != 0) or (second % smaller != 0):
        smaller = smaller - 1
    print ("Greatest Common Divisor is: " + str(smaller))
