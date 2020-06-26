
annual_salary = float(input("Annual salary:"))
portion_saved = float(input("Portion saved as percentage:"))
total_cost = float(input("Total cost:"))

#down payment and amount saved monthly
down_payment = total_cost*0.25
monthly_salary = annual_salary/12
amount_saved_monthly = portion_saved*monthly_salary


def compute_duration():
    #finding the number of months
    epsilon = 0.0001
    current_savings = 0
    #increment = 0.0001
    r=0.04
    months=0
    
    while abs(current_savings-down_payment)>= epsilon and current_savings < down_payment:
        current_savings= current_savings+current_savings*r/12 + amount_saved_monthly
        months+=1
    
    return months
print("Number of months", compute_duration() )
