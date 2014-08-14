#the following line's %d returns the 10 at the end of the line
x = "There are %d types of people." % 10
#sets the var called "binary" to the string value "binary"
binary = "binary"
#a lame joke in which the variable "do_not" is set to the value "don't"
do_not = "don't"
#sets 'y' to a string value while referencing the global variables at the end respectively
y = "Those who know %s and those who %s." % (binary, do_not)

#prints the content of the global variable "x"
print x
#prints the content of the global variable "x"
print y

#prints a given string. %r is set to the value "x" %r is the "same" as %s but is used for debugging, prints "raw data"
print "I said: %r," % x
#prints the string containing the string "y"
print "I also said: '%s'." % y

#sets the state of the boolean var hilarious to false/all functions using hilarious will return "False"
hilarious = False
#sets the string "joke_evaluation" to the quoted text and %r can be replaced with any var declared at the end of the line with "% "
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the string "joke_evaluation" and fills the %r with the boolean "hilarious"
print joke_evaluation % hilarious

# declares a string
w = "This is the left side of..."
# declares a string	
e = "a string with a right side."

# prints 2 strings "w" and "e" sequentially
print w + e

