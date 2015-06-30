from sys import argv
script, filename = argv
#Sys is a package, this phrase just says get the argv feature
#from that package.

txt = open(filename)
#Opens the file inside terminal by using txt. 
#It takes a parameter and returns value you can set to your own #variable.

print "Here's your file %r:\n" % filename
print txt.read()
#You give file a command by using the '.'. Difference is 'txt.read'
#says "Hey txt! Do your read command with no parameters!"

print "Type the filename again:"
file_again = raw_input("> ")
#raw_input("> ") linked to string (file_again).

txt_again = open(file_again)
#Once you've typed in filename, it is linked to another string 
#(txt_again) which means line below is opened by use of .read()

print txt_again.read()

txt.close()
txt_again.close()
