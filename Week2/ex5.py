## 99 Bottles of beer on the wall##


b = 99 # set bottles to 99

while b >  0:
    if b > 1: # if more than 1 bottles
        b_minus = b-1
        print (f"{b} of beer on the wall, {b} numbers of beer, take one down, pass it arround {b_minus} of beer on the wall!")
        b = b-1

    elif b == 1: # if one bottle
        print (f"1 bottle of beer on the wall, 1 bottle of beer! So take it down, pass it around, no more bottles of beer on the wall!")
        b = b-1

 # if no bottles
print ("No more bottles of beer on the wall, no more bottles of beer. Go to the store and go buy some more, 99 Bottles of beer on the wall!")
