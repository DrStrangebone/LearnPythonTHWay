def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
#Understood all of the defs above.
    
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d. Height: %d. Weight: %d. IQ: %d." % (
    age, height, weight, iq)

# A puzzle for extra credit. Type it in anyway.

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#inside out means deep within brackets it all starts there and you do it from inside out.

print "That becomes: ", what, "Can you do it by hand?"

answer = 24 + 34 / 100 - 1024

print answer 

#PEDMAS. Divison goes first, 34 / 100 = 00.34. Since there's no floating point, it's 0. 
# 24 - 1024 = -999.
