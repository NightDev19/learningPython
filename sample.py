name = "Kj"
age = 17
#      True         False      
if not name == "Kj" or not age == 15:
    print("Hello Kj")
else:
    print("Hello Stranger")
    
'''
Truth Table
AND Both conditions are true
X Y    Z
T T    T
F T    F
T F    F
F F    F

XAND Both conditions are false
if not condition1 and condition2:
X Y    Z
T T    F
F T    F
T F    F
F F    T

OR At least one condition is true
X Y    Z
T T    T
F T    T
T F    T
F F    F


XOR At least one condition is false
X Y    Z
T T    F
F T    T
T F    T
F F    T

if not condition1 or condition2:

NOR Its either both conditions are true
X Y    Z
T T    T
F T    F
T F    F
F F    F

if condition1 and condition2 or condition3 and codition4:

'''