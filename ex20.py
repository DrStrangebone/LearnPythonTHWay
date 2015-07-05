from sys import argv
#from system, unpackages argv.

script, input_file = argv
#etting the variables.

def print_all(f):
    print f.read()
#defining print_all(f) function.
#   prints out f.read().
# read is function. Returned as string. 

def rewind(f):
    f.seek(0) #seek IS A FUNCTION.
    #Moves to new file position.
#defing rewind(f) function.
    
def print_a_line(line_count, f):
    print line_count, f.readline()
#defining print_a_line(line_count, f)
#   prints out lint_count, f.readline()
    
current_file = open(input_file)
#input_file isn't defined? Look at argv. It is.

print "First let's print the whole file:\n"
#Any line ending in the input file will be seen as a '/n'.
f.r
#f.r?????
print_all(current_file)
#prints out open(input_file).

print "Now let's rewind, kind of like a tape."

rewind(current_file)
#Seek is what's happening.

print "Let's print three lines: "

current_line = 1
print_a_line(current_line, current_file)
#adds a number next to the 3 current_lines.

current_line = current_line + 1
print_a_line(current_line, current_file)
#Same as above but iterated.

current_line = current_line + 1
print_a_line(current_line, current_file)
#Same as above but iterated.

# the numbers to the left are what caused 1, 2, 3.
