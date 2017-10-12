## home cost calculator ##
print ("lets calculate how long it will take to save up for a house deposit including a semi-annual raise")

#input variables#
annual_salary       = float(input ("Enter your annual salary: "))
portion_saved       = float(input("Enter the percent of your salary to save, as a decimal: "))

total_cost          = float(input("Enter the total cost of your dream home: "))
semi_annual_raise   = float(input("Enter semi-annual raise, as a decimal: "))


#define variables#
portion_deposit     = (total_cost / 100) * 20
monthly_salary      = annual_salary/12
monthly_contrib     = monthly_salary * portion_saved
current_savings     = float(0)
months_passed       = int(0)
interest_rate       = 0.04 #rate of return

#computation loop#
while current_savings < portion_deposit:
    current_savings  = current_savings + current_savings*interest_rate/12    #add interest from previous months
    current_savings  = current_savings + monthly_contrib                     #add monthly contribution from salary
    months_passed    = months_passed   + 1                                   #increment month counter

    if months_passed % 6 == 0 :
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary      = annual_salary/12

print (f"Number of months: {months_passed}")                                #output number of months
