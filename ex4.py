cars = 100 #the = is for variable declarations. I declared them at the top here and then later when I call them some perform maths.
space_in_a_car = 4.0 #4.0 is a floating point number. Using the decimal makes python include non-integers in the equation instead of rounding off to ints
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity =  cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available." #here outside the quotes I call my first variable "cars" which I set to equal 100.
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers,"to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
