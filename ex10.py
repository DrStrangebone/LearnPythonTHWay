tabby_cat = "\tI'm tabbed in."
#/t means tabbed. It indents a space forward just like pressing tab button.
persian_cat = "I'm split\non a line"
#\n creates a new line.
backslash_cat = "I'm \\ a \\ cat."
#Double backslash = one backslash. What's any use to this when I could use double quotes?

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

#What happened here is: List was created by use of \t. 
#At the last list, \n\t means \n created a new space below, 
#with \t indenting it.

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True: 
    for i in ["/", "-", " | ", "\\" , " | " ]:
        print "%s\r" % i,

#print functions.
