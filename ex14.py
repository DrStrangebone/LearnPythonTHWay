from sys import argv
#import argument from system

script, user_name, last_name = argv
prompt = '> '
#create argument, string prompt.

print "Hi %s, I'm the %s script." % (user_name, script)
#%s means showing display. %r is for debugging to my understanding.
print "I'd like to ask you few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
#user_name is linked by use of %. 

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)


print """
Alright, so you said %r about liking me. You live in %r.
Not sure where that is. And you have a %r computer. Naice.""" % (likes, lives, computer)

last_name = raw_input("What was your last name? ")
print "Oh I remember you now Mr %s, on that bombshell, goodnight!" % (last_name)



#(Study drill) I tried entering fewer than three arguments. 
#Saw the error. It means I need to enter sufficient amount of value
# for argv. 
