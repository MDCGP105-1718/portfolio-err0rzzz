##function definition testing ##
x = 1

def f_fizz (x):

    """
    Checks if number is divisible by 3
    outputs Fizz if it is
    """
    if x % 3 == 0:
        print ("Fizz")
    else:
        print (x)

    return (x)

def f_buzz(x):

    """
    Checks if number is divisible by 5
    outputs Buzz if it is
    """

    if x % 5 == 0:
        print ("Buzz")
    else:
        print (x)

    return (x)

def f_fizzbuzz(x):
    """
    checks if number is divisible by both 3 and 5
    outputs fizzbuzz if it is
    """
    if x %3 == 0:
        if x %5 == 0:
            print ("fizzbuzz")
    return x

while (x<100):
    f_fizz(x)
    f_buzz(x)
    f_fizzbuzz(x)
    x += 1
