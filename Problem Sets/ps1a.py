# -*- coding: utf-8 -*-
"""
Alec Dewulf
Problem Set 1a
Time Spent 0.5 hours
Created on Fri Jan  3 11:14:02 2020

"""
 
annual_salary = int(input("Enter you annual salary: " ))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))


portion_down_payment = 0.25
current_savings = 0
r = 0.04
additional = current_savings*r/12
monthly_salary = annual_salary / 12

num_months = 0

while current_savings < total_cost * portion_down_payment:
    additional = current_savings*r/12
    current_savings += monthly_salary * portion_saved + additional
    num_months += 1


print(num_months)
