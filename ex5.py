name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
height_metric = height * 0.0254 # Takes the inches from the heigh var and converts to meters.
weight = 180.0 # lbs
weight_metric = weight * 0.453592 # Takes imperial version "weight" and converts it to kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %g meters." % height_metric
print "He's %d pounds heavy or %g kilograms for the rest of the world." % (weight, weight_metric)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
