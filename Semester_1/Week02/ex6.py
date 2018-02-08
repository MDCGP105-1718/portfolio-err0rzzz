## input tests ##
#define variables and prompt for them
print ("Please input the following data followed by enter")
name            = input ('Enter your name: ')
age             = int(input ('how old are you?: '))
height_inches   = int(input ("in inches, how tall are you?: ")) #inches
weight_pounds   = int(input ("in pounds, how much do you weigh?: "))          #pounds
eyes            = input ("what colour are your eyes?: ")
hair            = input ("what colour is your hair?: ")
heavy           = weight_pounds > 3000 #sets boolean output on heavy based on weight_pounds being greater than 3000
sigma_i         = age + height_inches + weight_pounds

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
sigma_m         = age + height_cm + weight_kg
bmi             = height_cm / (weight_kg * weight_kg)

##metric output##
print (f"now let's talk about {name}. using the Metric system")
print (f"He is arround {height_cm} centimeters tall.")
print (f"He's {weight_kg} kilograms in weight.")
print(f"If I add {age}, {height_cm} and {weight_kg} I get {sigma_m}")

##checks##
##retirement check##
if age > 17 and age < 75:
    print ("you're of working age")
elif age < 17:
    print ("you're too young to work!")
else:
    print ("you're retired, congratulations!")

##bmi aka body self loathing scale##
print (f"your BMI is {bmi}")
if bmi < 18.5:
    print ("this is underweight")
elif bmi >= 18.5 and bmi < 25:
    print ("this is a healthy BMI")
elif 25 <= bmi < 30:
    print ("this is above ideal range")
else:
    print ("your BMI is considered overweight")
