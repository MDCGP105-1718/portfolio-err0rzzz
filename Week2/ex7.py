## home cost calculator ##
print ("lets calculate how long it will take to save up for a house")
#input variables#
annual_salary   = float(input ("Enter your annual salary: "))
portion_saved   = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost      = float(input("Enter the total cost of your dream home: "))

#define variables#
portion_deposit = (total_cost / 100) * 20
monthly_salary  = annual_salary/12
monthly_contrib = monthly_salary * portion_saved
current_savings = float(0)
months_passed   = int(0)
r               = float(0.04)

while current_savings < portion_deposit:
    current_savings = current_savings + current_savings*r/12    #add interest from previous months
    current_savings = current_savings + monthly_contrib         #add monthly contribution from salary
    months_passed   = months_passed   + 1                       #increment month counter

print (f"Number of months: {months_passed}")                    #output number of months
