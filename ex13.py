# argv is a module, it allows me to add arguments 
# at the end when I run the .py from command line
from sys import argv

#line 7 tells sets the number of arguments I can import
#from command line. Must be the exact or it errors
script, first, second, third, fifth = argv

#the vars at the end are calling the arguments from argv by name
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is :", third
print "Your failure to count is identified by:", fifth

