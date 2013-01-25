# Filename: q1_fahrenheit_to_celsius.py
# Author: Lim Ying Wei
# Created: 20130122
# Modified: 20120122
# Description: Program to convert fahrenheit to celsius

# main

# promt and get temperature in fahrenheit
fahrenheit = float(input("Enter Temperature in F: "))

# calculate temperature
Temperature = (fahrenheit - 32) * (5/9) 

# display results
print("Celsius= {0:.1f}".format(Temperature) + "°C")
