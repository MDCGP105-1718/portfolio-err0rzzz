## input tests ##


#define variables and prompt for them
print ("Enter your name")
name            = input ('-->')
print ("how old are you?")
age             = input ('-->')            
print ("how tall are you? (in inches)")
height_inches   = input ('-->')             #inches
print ("how much do you weigh? (in pounds)")
weight_pounds   = input ('-->')             #pounds

print ("what colour are your eyes?")
eyes            = input ('-->')

print ("what colour is your hair?")
hair            = input ('-->')

heavy           = weight_pounds > 3000 #sets boolean output on is_heavy based on my_weight being greater than 3000
sigma_i           = age + height_inches + weight_pounds

##output##
print (f"Let's talk about {name} using the Imperial system.")
print (f"He is arround {height_inches} inches tall.")
print (f"He's {weight_pounds} pounds.")
print (f"It would be {heavy} to say that he is overweight.")
print (f"He's got {eyes} eyes and {hair} hair.")

print(f"If I add {age}, {height_inches} and {weight_pounds} I get {sigma_i}")

##convert to metric
height_cm       = height_inches * 2.54
weight_kg       = weight_pounds * 0.45359237
sigma_m           = age + height_cm + weight_kg

##metric output##
print (f"now let's talk about {name}. using the Metric system")
print (f"He is arround {height_cm} centimeters tall.")
print (f"He's {weight_kg} kilograms in weight.")

print(f"If I add {age}, {height_cm} and {weight_kg} I get {sigma_m}")
