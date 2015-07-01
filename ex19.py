#cheese_and_crackers is main defintion, being cheese_count and
#boxes_of_crackers variables.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly: "
cheese_and_crackers(20,30)


print "OR, we can use variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#cheese_and_crackers unpacked by amount_of_cheese, amount_of_crackers,
#then those two variables is assigned by a number (= 10/ = 50.) 
#Don't know why but I see this messy.

print "We can even do maths inside too: "
cheese_and_crackers(10 + 20, 5 + 6)
#this one is a lot more simplified. It happens in bracket.
#( x + y, i + j) - This comma is magical.


print "And we can combine the two, variables and maths: "
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#Combining the two.

#STUDY DRILL TIME

def tardis(doctor_who_r, companions, K_9):
    print "You have %d companions!" % companions_count
    print "You have %d K9." % K_9_count
    print "How many regenerations have you had? %d" % doctor_who_regen
    print "You do know who you are right, sir?\n"
    print "%s " % dr_who_name
    
companions_count = 2
K_9_count = 1
doctor_who_regen = 12
dr_who_name = ("Yes, I'm the Doctor. Doctor who. *cue Dr Who theme*")
tardis(companions_count, K_9_count, doctor_who_regen)
