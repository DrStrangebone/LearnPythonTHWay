from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying rom %s to %s" % (from_file, to_file)

#We could do these two on one line. How?

in_file = open(from_file); indata = in_file.read()
#Opens an from_file (from terminal) and indata reads it.

print "The input file is %d bytes long." % len(indata)

print "Does the output file exists? %r" % exists(to_file)
#'exists' is False at this stage because it has not been created.
#After this, it will have been created.

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("> ")
#How does this work?

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
#Why did I have to close this? Will come back to this.
in_file.closed()


