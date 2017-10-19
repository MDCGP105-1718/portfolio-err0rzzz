##function definition testing ##
x = 1

def f_fizzbuzz(x):
    """
    checks if number is divisible by both 3 and 5
    outputs fizzbuzz if it is
    """
    if x %3 == 0:
        if x %5 == 0:
            print ("fizzbuzz")
        else:
            print ("Fizz")
    elif x %5 == 0:
        print ("Buzz")
    else:
        print (x)

    return x

while (x<101):
    f_fizzbuzz(x)
    x += 1
