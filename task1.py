print "Russ' ridiculously expensively simple calculator!!"

numb1 = raw_input("What is the first number? ")
oper = input("What operator do you want to use? (*, /, +, -) ")
numb2 = raw_input("What is the second number? ")

if oper == '*':
    total = numb1 * numb2
    print "Answer: ", total
elif oper == '+':
    total = numb1 + numb2
    print "Answer: ", total
elif oper == '-':
    total = numb1 - numb2
    print "Answer: ", total
elif oper == '/':
    total = numb1 / numb2
    print "Answer: ", total
else:
    print "ERROR - INFORMATION NOT CORRECT."
