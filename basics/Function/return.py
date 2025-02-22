'''
Return Function Statement

Syntax:

def function_name(parameters):
    statements
    return statement
    
function_name(arguments)
'''

def add(n1,n2):
    return n1 + n2

sum = add(2,3) # Assigning the return value to a variable
print(sum) # Printing the variable

def isLegalAge(age):
    if age >= 18:
        return True
    else:
        return False

isLegal = isLegalAge(17)
print(isLegal)