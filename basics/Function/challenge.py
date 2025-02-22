'''
- **Challenge**
    
    **Square a Number** with **Function w/ Parameter**
    
    Create a Program that will make the user input a number the program should **Square** the number then print it 
    
    **Condition**
    
    - You must create a function called **square()** then pass the number inside it then return the squared value
    - **Print** the square value outside of the function
    
    **Example**
    
    Input : 5
    Output : 25
'''

def square(num):
    return num * num

num = int(input("Enter a number: "))
print(f"The square of {num} is {square(num)}")