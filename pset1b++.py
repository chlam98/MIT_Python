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


#passing all arguments to function to compute needed months, so the global variables value is not change 
#so they can be reused in compute current_saving info. 
def compute_duration(rate, annual_salary, portion_saved, semi_annual_raise, total_cost, down_payment):
    #referenced to global variables to avoid local reference conflict. 
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
    

#Compute savings based on necessary info.
#For bisection algorithms, we can compute current savings based on different interest rate.
#if current savings is larger than downpayment, then we decrease interest rate, 
#otherwise we increase interest rate. This operation can keep going until the different between 
#current_savings and down_payment is small enough. 
def compute_savings(rate, annual_salary, portion_saved, semi_annual_raise, months): 
    #referenced to global variables to avoid local reference conflict. 
    #finding the number of months
    current_savings = 0
    monthly_salary = annual_salary/12
    counter = 0
    
    while counter < months:
        counter += 1
        if counter % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
            monthly_salary = annual_salary/12
        amount_saved_monthly=portion_saved*monthly_salary
        current_savings= current_savings+current_savings*rate/12 + amount_saved_monthly
    return current_savings


months = compute_duration(r, annual_salary, portion_saved,semi_annual_raise,total_cost, down_payment )
print("Number of months", months)

print("current saving after ", months , " is: " , compute_savings(r, annual_salary, portion_saved, semi_annual_raise, months))
