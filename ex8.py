formatter = "%r %r %r %r"
#4 formatters.

print formatter % (1, 2, 3, 4)
#int attached to formatters.
print formatter % ("one", "two", "three", "four")
#strings attached to formatters - by word.
print formatter % (True, False, True, False)
#statements attached to formatters. 
print formatter % (formatter, formatter, formatter, formatter)
#Formatter iteration, NOT by % but by literal 'formatter' atatched by %.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
#4 % = 4 lines = small poem.

#Mistakes: Not looking thoroughly on original code. Missed out certain single quotes and double quotes because I skimmed through - easy to miss. 

#Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?

#I think it is because of True, False statements.
