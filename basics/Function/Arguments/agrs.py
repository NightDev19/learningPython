'''
Arbitrary Arguments
*args and **kwargs are special variables that allow you to pass any number of arguments to a function.

*args is a tuple and **kwargs is a dictionary.

syntax

def function_name(*args):
    statements
    
function_name(arguments)
'''

def my_function(*args):
    for i in args:
        print(i)
    
my_function(1,2,3,4,5)

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
my_function(name="John", age=25)