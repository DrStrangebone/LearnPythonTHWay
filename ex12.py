name = raw_input ("Name: ")
#Unlike last lesson, it contains parenthesis. It 'strings' along (for #lack of better words) with variable for input.
age = raw_input("How old are you? ")
#Same as above but age.
height = raw_input("How tall are you? ")
#Same as above but height.
weight = raw_input("How much do you weigh? ")
#Same as above but weight

print "So your name is %r, %r years-old, %r tall and %r heavy." % (
    name, age, height, weight)
    
#%r IS FOR DEBUGGING AND IS 'RAW REPRESENTATION' WHILE %s IS FOR DISPLAY.
#REMEMBER THIS!!!!
