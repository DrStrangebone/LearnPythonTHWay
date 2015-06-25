print "Mary had a little lamb."
#Obvious print.
print "Its fleece was white as %s." % 'snow'
# '%s' links to snow. 'snow' is NOT a variable.
# A variable wouldn't have the single-quotes around it.

print "And everywhere that Mary went."
#Obvious print.

print "." * 10 #What'd it do?
#It printed out 10 dots, . * 10 = ..........

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
#Strings.

#Watch that comma at the end, try removing it to see what happens.

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# With commas, it comes up as 'Cheese Burger'.
# Without commas, it appears this: Cheese
#                                  Burger
#So I assume commas are important to link one another 
#into the same sentence.
