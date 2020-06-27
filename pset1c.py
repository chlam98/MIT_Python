
###PSET.1B
annual_salary = float(input("Annual salary:"))
total_cost = 1000000
semi_annual_raise = 0.07
rate = 0.04

#down payment
down_payment= total_cost*0.25
months = 36


#For bisection algorithms, we can compute current savings based on different portion_saved rate.
#if current savings is larger than down payment, then we decrease portion_saved rate, 
#otherwise we increase portion_saved rate.
def compute_savings(rate, annual_salary, portion_saved, semi_annual_raise, months): 
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



def get_savingRate(rate, annual_salary, semi_annual_raise, down_payment, months):
    high_rate = 10000 
    low_rate = 0    
    current_rate = 0
    
    #if the annual_salary is too large, the error_range must be large as well, otherwise
    #bisection algorithms could enter infitite loop. 
    error_range = 100 
    
    current_savings = 0
    bisect_counter = 0
    
    #To check the annual salary is too low to save enough down payment in three years. 
    current_savings = compute_savings(rate, annual_salary, high_rate/10000, semi_annual_raise, months)
   
    if( current_savings < (down_payment - error_range)):
        print("can't save enough down payment in 3 years")
        return #terminate the routine, otherwise will go to while loop which may cause inifite loop.

    
    while abs(current_savings - down_payment) > error_range:
        current_rate = int((high_rate + low_rate) / 2)
        current_savings  =  compute_savings(rate, annual_salary, current_rate/10000, semi_annual_raise, months)
        bisect_counter += 1
        #if current savings is larger than down_payment, the high_rate need to be lowered to current rate  
        #so next round current_rate is decreased, current_savings will be decrease as well. 
        if(current_savings > down_payment ):
            high_rate = current_rate 
        else:
            low_rate = current_rate
            
        #un-comment following two lines to exam each iteration result.   
        #print("high_rate ", high_rate, " low_rate ", low_rate, "current rate ", current_rate)
        #print("current savings ", current_savings)
    print("best saving rate is ",current_rate/10000)
    print("bisection steps is: ", bisect_counter)
   
    
get_savingRate(rate, annual_salary, semi_annual_raise, down_payment, months)