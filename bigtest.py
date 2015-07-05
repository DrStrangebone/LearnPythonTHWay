#THIS WILL BE CONSTANTLY UPDATED IN THE NEXT FEW DAYS.


from sys import argv

'''
import adds modules to your script, rather than giving you all at once,
it asks what you plan to use. 
Acts as documentation for other programmers to see your code.
'''

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third, "\n"



myname = "DrStrangebone"
lines = 45

print "This is big quiz for %s." % myname
print "How many lines do you think you'll achieve? At least %d lines." % lines
print "How many bytes does this %s have? %d" % (myname, len(myname)) 

joke = "Want to hear a joke? True or False: %r"
nope = False 

print joke % nope

#Formatters understood. Print understood.

print "\nNewline.\t Tabline."


    
    
