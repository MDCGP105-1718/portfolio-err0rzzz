##function definition testing ##
x = 1

def f_fizz (x):
    """
    Checks if number is divisible by 3
    outputs Fizz if it is
    """

    if x %3 == 0:
        then print ("Fizz")
        else print (x)

    x +=1
    return (x)

def f_buzz(x):
        if x %5 == 0:
            then print ("Buzz")
            else print (x)

        x +=1
        return (x)

while (x<100):
    f_fizz (x)
    f_buzz (x)
