##Random implimentation##
from random import randint

x = randint (0,100)

guess            = int(input ('guess a number between 0-100:'))

if guess == x:
    print ("you got it!")

elif guess > x:
    print ("too high")

else:
    print ("too low")
