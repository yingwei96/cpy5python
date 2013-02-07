# Filename: q08_top2_scores.py
# Author: Lim Ying Wei
# Created: 20130203
# Modified: 20130203
# Description: Program to find top 2 scores

students = int(input("Enter number of students: "))

i = 0
top = 0
second = 0
topname = str("name")
secondname = str("name2")
running = True

while (students > i):
    name = str(input("Enter name of student: "))
    score = int(input("Enter score of " + str(name) + ": "))
    i = i + 1
    
    if students == i:
        running = False
        print((topname) + " has the highest score of " + str(top))
        print((secondname) + " has the second highest score of " + str(second))

    elif top <= score:
        second = int(top)
        secondname = str(topname)
        top = int(score)
        topname = str(name)
        
    elif top >= score and second <= score:
        top = int(top)
        topname = str(topname)
        second = int(score)
        secondname = str(name)

    elif top >= score and second >= score:
        top = int(top)
        topname = str(topname)
        second = int(second)
        secondname = str(secondname)
