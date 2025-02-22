'''
kwargs is a special variable that allows you to pass keyword arguments to a function.

**kwargs is a dictionary.

Syntax

def function_name(**kwargs):
    statements
    
function_name(key1=value1, key2=value2)
'''


def printStudent(**student):
    print(f"Name : {student['name']}")
    print(f"Age  : {student['age']}")

printStudent(name="John", age=25)