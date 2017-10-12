## home cost calculator ##
print ("lets calculate how what percenatge of income is needed to save for a house")

#input variables#
annual_salary       = float(input ("Enter your annual salary: "))

#define variables#
total_cost          = float(1000000))                                       #set cost of house
semi_annual_raise   = float(0.07)                                           #set semi annual raise
interest_rate       = 0.04                                                  #rate of return
months_passed       = 36                                                    #define months passed

portion_deposit     = (total_cost / 100) * 25                               #set deposit to 25% of house cost
monthly_salary      = annual_salary/12                                      #set monthly salary
monthly_contrib     = monthly_salary * portion_saved                        #set ammount to increase savings by each month
current_savings     = float(0)                                              #define savings as a float
portion_saved       = float(0)                                              #defne percentage to save as a float



#computation loop#
while current_savings < portion_deposit:
    current_savings  = current_savings + current_savings*interest_rate/12    #add interest from previous months
    current_savings  = current_savings + monthly_contrib                     #add monthly contribution from salary
    months_passed    = months_passed   + 1                                   #increment month counter

    if months_passed % 6 == 0 :
        annual_salary  += annual_salary*semi_annual_raise
        monthly_salary  = annual_salary/12
        monthly_contrib = monthly_salary * portion_saved

print (f"Number of months: {months_passed}")                                #output number of months
