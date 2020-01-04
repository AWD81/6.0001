# -*- coding: utf-8 -*-
"""
Alec Dewulf
Problem Set 1c
Time Spent: 1 hour
Created on Fri Jan  3 17:49:00 2020

"""
# Getting user inputted values
starting_salary = int(input("Enter the starting salary: "))

# cloning of starting_salary so the amount isn't lost when it's redefined
# in the loop
salary = starting_salary

# Predetermined values
semi_annual_raise = 0.07
annual_return = 0.04
monthly_return = annual_return/ 12
total_cost = 1000000
down_payment = total_cost * 0.25

monthly_salary = salary / 12

# number of months to pay and degree of error
month = 0
epsilon = 100
counter = 0

# setting the low and high conditions
low = 0
high = 1

savings_rate = 0
amount_saved = 0
# Bisection search to find the best savings rate
while abs(amount_saved - down_payment) >= epsilon:
    # reset the amount saved after it's been tested
    amount_saved = 0
    # looping through 3 years to check amount saved with the
    # corrosponding savings_rate
    while month != 36:
        month += 1
        # amount from return
        amount_from_return = amount_saved * monthly_return
        # add the amount from working
        amount_saved += (savings_rate * monthly_salary) + amount_from_return

        if month % 6 == 0:
            salary *= (1 + semi_annual_raise)
            monthly_salary = salary / 12
        
    # guess was too low 
    if amount_saved < down_payment:
        low = savings_rate
    # guess was too high
    elif amount_saved > down_payment:
        high = savings_rate
    
    # condition is called when 100% of the salary isn't enough
    if savings_rate == 1:
        print("It is not possible to pay the down payment in three years")
        break
        
    # next savings rate to try is in the middle
    savings_rate = (high + low)/2
    # reset values and increase counter by one
    counter += 1
    month = 0
    salary = starting_salary
    
# print results
print("Best savings rate: ", savings_rate)
print("Steps in bisection search:", counter)
   
