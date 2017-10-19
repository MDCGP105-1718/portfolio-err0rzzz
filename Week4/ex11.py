##Random implimentation##
from random import randint
x = randint (0,100)

guess            = int(input ('guess a number between 0-100:'))
y = 1

def check_guess(x):
    if guess > x:
        print ("too high")
    elif guess < x:
        print ("too low")
    return (x)

while guess - x !=0:
    check_guess(x)
    guess            = int(input ('enter a new guess: '))
    y += 1
    if guess == x:
        print (f"you got it! in {y} guesses")
