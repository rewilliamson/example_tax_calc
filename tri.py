#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:24:47 2022

@author: rewilliamson
"""


income = float(input('Enter income: ')) # Take user input

# Determine tax bracket

if income > 523600:
    bracket = 7
elif income > 209425:
    bracket = 6
elif income > 164925:
    bracket = 5
elif income > 86375:
    bracket = 4
elif income > 40525:
    bracket = 3
elif income > 9950:
    bracket = 2
elif income > 0:
    bracket = 1
    
else:
    bracket = 0 # Catch cases of 0 or negative input
    
# Initialize variables for later use in case they aren't defined in the while statement
income_rem = income
tax_37 = 0
tax_35 = 0
tax_32 = 0
tax_24 = 0
tax_22 = 0
tax_12 = 0
tax_10 = 0
 
while bracket > 0:
    if bracket == 7:
        tax_37 = (income - 523600) * 0.37
        income_rem = 523600
        bracket -= 1
    elif bracket == 6:
        tax_35 = (income_rem - 209425) * 0.35
        income_rem = 209425
        bracket -= 1
    elif bracket == 5:
        tax_32 = (income_rem - 164925) * 0.32
        income_rem = 164925
        bracket -= 1
    elif bracket == 4:
        tax_24 = (income_rem - 86375) * 0.24
        income_rem = 86375
        bracket -= 1
    elif bracket == 3:
        tax_22 = (income_rem - 40525) * 0.22
        incom_rem = 40525
        bracket -= 1
    elif bracket == 2:
        tax_12 = (income_rem - 9950) * 0.12
        income_rem = 9950
        bracket -= 1
    elif bracket == 1:
        tax_10 = income_rem * 0.10
        income_rem = 0
        bracket -= 1
    else:
        break
    
    
total = tax_37 + tax_35 + tax_32 + tax_24 + tax_22 + tax_12 + tax_10
        
        
    
    
