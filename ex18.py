#This one is like your scripts with argv
def print_two(*args):
#args is bundled up.
#stretch into two 1 & 2 args = args
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#Main arg is connected by two args

#Ok, that *argsis actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#A lot more simple to understand. String for string.

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#Same as above.
    
# this one takes no arguments
def print_none():
    print "I got nothin'."

#No args.

print_two("Zed","Shaw")
#Defined.
print_two_again("Zed","Shaw")

print_one("Hi!")

print_none()


