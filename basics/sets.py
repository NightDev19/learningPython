
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
print(evenNumbers,"12 is added")

# Adding Items to a Set using update()
print("\nAdding Items to a Set using update()")
extension = [12,14,16,18,20]
evenNumbers.update(extension)
print(evenNumbers,"adding an Extension")

# Deleting Items from a Set using remove()
print("\nDeleting Items from a Set using remove()")
evenNumbers.remove(20)
print(evenNumbers,"20 is removed")

# Deleting Items from a Set using discard()
print("\nDeleting Items from a Set using discard()")
evenNumbers.discard(18)
print(evenNumbers,"18 is removed")

# Delete item from a Set using pop()
print("\nDelete item from a Set using pop()")
evenNumbers.pop()
print(evenNumbers,"2 is removed")

# Clearing a Set using clear()
print("\nClearing a Set using clear()")
evenNumbers.clear()
print(evenNumbers,"Set is cleared")

# Copying a Set using copy()
print("\nCopying a Set using copy()")
setOne = {1,2,3,4,5,6,7,8,9,10}
setTwo = setOne.copy()
print(setOne)
print(setTwo)

# Combining Sets
print("\nCombining Sets")
setOne = {1,2,3,4,5,6,7,8,9,10}
setTwo = {11,12,13,14,15,16,17,18,19,20}
setThree = setOne.union(setTwo)
print("Set One: ",setOne)
print("Set Two: ",setTwo)
print("Union: ",setThree)

# Difference between Sets
print("\nDifference between Sets")
setOne = {1,2,3,4,5,6,7,8,9,10}
setTwo = {1,11,12,13,14,15,16,17,18,19,20}
setThree = setOne.difference(setTwo)
print("Set One: ",setOne)
print("Set Two: ",setTwo)
print("Difference: ",setThree)

# intersection between Sets
print("\nIntersection between Sets")
setOne = {1,2,3,4,5,6,7,8,9,10}
setTwo = {1,11,12,13,14,15,16,17,18,19,20}
setThree = setOne.intersection(setTwo)
print("Set One: ",setOne)
print("Set Two: ",setTwo)
print("Intersection: ",setThree)