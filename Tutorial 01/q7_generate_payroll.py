# Filename: q7_generate_payroll.py
# Author: Lim Ying Wei
# Created: 20130124
# Modified: 20120124
# Description: Program to get payroll

# main

# promt and get name
name = (input("Enter Name: "))

# prompt hours worked
hours = float(input("Enter Number Of Hours Worked Weekly: "))

# prompt pay rate
pay = float(input("Enter Hourly Pay Rate: "))

# prompt CPF
cpf = int(input("Enter CPF Contribution Rate(%): "))
            
# calculate gross pay
gross = hours*pay
con = gross/100*cpf
net = gross-con          

# display results
print ("Payroll statement for {0:}".format(name))
print ("Number Of Hours Worked in Week= {0:}".format(hours))
print ("Hourly Pay Rate: $" + "{0:.2f}".format(pay))
print ("Gross Pay= $" + "{0:.2f}".format(gross))
print ("CPF Contribution at " + "{0:}".format(cpf) + "% = $" + "{0:.2f}".format(con))
print ("Net Pay= $" + "{0:}".format(net))
