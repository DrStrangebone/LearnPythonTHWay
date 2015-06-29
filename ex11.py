print "How old are you?",
#print output
age = raw_input()
#Text input, do not forget the 'raw_' bit. NOT an integer. 
#Needs (int(raw_input)) to do that.
print "How tall are you?",
#print output
height = raw_input()
#Non-int input.
print "How much do you weigh?",
#Print output
weight = raw_input()
#non-int input.
print "So you're %r old, %r tall and %r heavy. Great." % (
    age, height, weight)
    
#%r's collect info in respetive order, age, height and weight.
#If I shuffle it around, it won't make sense. 
