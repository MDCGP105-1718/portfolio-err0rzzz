### Variables ###

##define variabeles##
cars = 100          #define cars
space_in_a_car = 4  #define space_in_a_car
drivers = 30        #define drivers
passengers = 90     #define total number of passengers

#compute variables#
cars_not_driven = cars - drivers                        #define cars_not_driven
cars_driven = drivers                                   #define drivers
carpool_capacity = cars_driven * space_in_a_car         #define cars_driven
average_passengers_per_car = passengers / cars_driven    #define average_passengers_per_car

#output#
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
