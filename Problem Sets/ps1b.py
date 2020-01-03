# -*- coding: utf-8 -*-
"""
Alec Dewulf
Problem Set 1b
Time Spent: 1 hour
Created on Fri Jan  3 11:14:02 2020

"""
# user supplied data
annual_salary = int(input("Enter you annual salary: " ))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))

# initially current_savings is 0
current_savings = 0

# fixed varialbes
portion_down_payment = 0.25
r = 0.04
additional = current_savings * r /12
monthly_salary = annual_salary / 12

num_months = 0
# using exhaustive enumberation to find the number of months needed
while current_savings < total_cost * portion_down_payment:
    num_months += 1
    additional = current_savings * (r /12)
    current_savings += monthly_salary * portion_saved + additional
    
    # salary increase occurs at the end of the month
    if num_months % 6 == 0:
        annual_salary *= 1 + semi_annual_raise
        monthly_salary = annual_salary/12

# print the number of months needed
print(num_months)
