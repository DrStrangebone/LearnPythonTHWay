from sys import argv
#sys is a package, this just says get the argv feature 
#from that package.

script, filename = argv
#unpacked arguments.

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL C (^C)"
#How does this work?
print "If you do want that, hit RETURN."
#And this?

raw_input("?")

print "Opening file..."
target = open(filename, 'w')
#'w' means open this file in 'write' mode thus the w character.
#There's also 'r' for read, 'a' for append and modifiers for these.

print "Truncating the file. Goodbye!"
target.truncate()
#Why open and then truncate the file? Clean slate?

print "Now I'm going to ask you for three lines."


line1 = raw_input("Line 1: \n")
line2 = raw_input("Line 2: \n")
line3 = raw_input("Line 3: \n")

print "I'm going to write these to the files."

target.write("%s\n%s\n%s" % (line1, line2, line3)) 

#'target.write(line#)' is pretty neat. The brackets links to another 
#string. 
print "And finally, we close it."
target.close()
