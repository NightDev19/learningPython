# Flow
'''
Flow:

1. Understading Sets
2. Manipulating Sets
'''

# Topic
'''
============
Sets
============
A Collection of Variables that is Partially Writable and it's Unordered and Unindexed

Syntax:
identifier = {value,value1,value2}
Example:
evenNumbers ={2,4,6,8,10} 


- You can read a sets by printing the whole set
- You can read a sets using a loop

* TODO: Reading Set ITEMS
    - It is not possible to read certain item in a set unless you cast it into a List or Tuple
    
    - hence Sets are unindexed or unordered
    
    Syntax :
        list(set)
        tuple(set)

* TODO: Assigning Set Items
    - It is not possible to change the value of a certain item in a set unless you cast it into a List or Tuple
    
    - hence Sets are unindexed or unordered
    
    Syntax :
        list(set)
        tuple(set)

'''

# Length of a Set
'''
===============
Set Length
===============
You can check the number of items in a set by using the len() function

Syntax:
print(len(set))
Example:
print(len(evenNumbers))

'''

# Adding Items to a Set
'''
===============
Set ADD ITEMS by add()
===============
add() adds an item at the END OF THE SET.

Syntax:
set.add(value)
Example:
evenNumbers.add(12)
'''

# Adding Items to a Set using update()
'''
===============
Set ADD ITEMS by update()
===============
update() allows multiple items to be added at the same time in the sets

Syntax:
set.update(value,value1,value2)
Example:
evenNumbers.update([12,14,16,18,20])
'''

# Deleting Items from a Set using remove()
'''
===============
Set DELETE ITEMS by remove()
===============
remove() deletes an item based on their value

Syntax:
set.remove(value)
Example:
evenNumbers.remove(20)

PS : if the value does not exist, it will throw an error

'''

# How to use a Sets
evenNumbers ={2,4,6,8,10} 
print(evenNumbers)
'''
it cannot be read individually

For example:
print(evenNumbers[0]) like this will not work
'''
#Reading a Sets using a Loop
print("\nUsing a loop")
for data in evenNumbers:
    print(data)

# Setting Set into a List
print("\nSetting Set into a List")
listSet = list(evenNumbers)
print(listSet)
# Setting Set into a Tuple
print("\nSetting Set into a Tuple")
tupleSet = tuple(evenNumbers)
print(tupleSet)

# Length of a Set using len() function
print("\nLength of a Set")
lenSet = len(evenNumbers)
print(lenSet)

# Adding Items to a Set using add()
print("\nAdding Items to a Set using add()")
evenNumbers.add(12)
print(evenNumbers)

# Adding Items to a Set using update()
print("\nAdding Items to a Set using update()")
extension = [12,14,16,18,20]
evenNumbers.update(extension)
print(evenNumbers)

# Deleting Items from a Set using remove()
print("\nDeleting Items from a Set using remove()")
evenNumbers.remove(20)
print(evenNumbers)