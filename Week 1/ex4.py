##printf string example##

#define variables
name            = 'Alex Mednick'
age             = 31                #:(
height_inches   = 71                #ishinches
weight_pounds   = 180               #pounds
eyes            = 'Brown'
hair            = 'Browner'
heavy           = weight_pounds > 3000 #sets boolean output on is_heavy based on my_weight being greater than 3000
sigma           = age + height + weight

##output##
print (f"Let's talk about {name}.")
print (f"He is {height_inches} inches tall.")
print (f"He's {weight} pounds heavy.")
print (f"It is {heavy} that he is overweight.")
print (f"He's got {eyes} eyes and {hair} hair.")

print(f"If I add {age}, {height} and {weight} I get {sigma}")
