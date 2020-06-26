"""
Created on Fri Jun 19 13:04:48 2020
@author: selina
"""
###PSET.1B
annual_salary = float(input("Annual salary:"))
portion_saved = float(input("Portion saved as percentage:"))
total_cost = float(input("Total cost:"))
semi_annual_raise = float(input("Semi annual salary raise:"))


#down payment
down_payment= total_cost*0.25

#interest rate
r = 0.04  

#passing rate as an augument
def compute_duration(rate):
    #referenced to global variables to avoid local reference conflict. 
    global annual_salary, portion_saved, semi_annual_raise, total_cost, down_payment;
    #finding the number of months
    epsilon = 0.0001
    current_savings = 0
    months=0
    
    
    while abs(current_savings-down_payment)>= epsilon and current_savings < down_payment:
        months+=1
        if months % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
            monthly_salary= annual_salary/12
        else:
            monthly_salary= annual_salary/12
        amount_saved_monthly=portion_saved*monthly_salary
        current_savings= current_savings+current_savings*rate/12 + amount_saved_monthly
    return months;

#call the compute_duration function with a specific rate to get the answer. 
print("Number of months", compute_duration(r))