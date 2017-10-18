## home cost calculator ##
print ("lets calculate how what percenatge of income is needed to save for a house")

#input variables#
annual_salary       = float(input ("Enter your annual salary: "))

#define variables#
total_cost          = 1000000                                               #set cost of house
semi_annual_raise   = float(0.07)                                           #set semi annual raise
interest_rate       = 0.04                                                  #rate of return
total_months        = 36                                                    #define months passed
months_passed       = 0

deposit             = (total_cost / 100) * 25                               #set deposit to 25% of house cost
monthly_salary      = annual_salary/12                                      #set monthly salary
#monthly_contrib     = monthly_salary * savings_rate                         #set ammount to increase savings by each month
current_savings     = float(0)                                              #define savings as a float
savings_rate        = float(0)                                              #defne percentage to save as a float



## define computation loops ##
epsilon = 100                           #acceptable margin of error: £100
num_guesses = 0                         #number of iterations
low = 0                                 #low threashold for bisection
high = deposit                          #set high threashold as the value of the cube to be found
guess = (high + low)/2.0                #find the half point to start the check and use it to make a guess

while abs(guess**3 - cube) >= epsilon:  #start a loop which checks if the guess is correct within epsilon margin
    if guess**3 < cube:                 #if guess guess cubed is less than guess, tharefore the guess is too low
        low = guess                     #so set the new low threashold as the guess
    else:                               #if not then that means the guess is too high
        high = guess                    #so set the new high threashold as the guess
    guess = (high + low) / 2.0          # make a new Bisection
    num_guesses += 1                    #increase the iteration counter

print('num_guesses =', num_guesses)                 #output number of iterations
print(guess, 'is close to the cube root of', cube)   #output answer

while months_passed < total_months:
    
