## bisection search to guess a number##

cube = 27                               #number to find root of
epsilon = 0.01                          #acceptable margin of error
num_guesses = 0                         #number of iterations
low = 0                                 #low threashold for bisection
high = cube                             #set high threashold as the value of the cube to be found
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
