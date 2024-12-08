# All Topics
"""
1. Understanding List
2. Manipulating List
3. Understanding Tuples
4. Reading Tuples

====================
Advance Data Types:
====================
list = x = [1,2,3,4,5]
tuple = x = (1,2,3,4,5)
set = x = {1,2,3,4,5}
dictionary = x = {"key1":"value1","key2":"value2","key3":"value3"}
frozenset = x = frozenset({1,2,3,4,5})
bytearray = x = bytearray(5)
bytes = x = b"Hello"
memoryview = x = memoryview(b"Hello")

*****IMPORTANT******
================
Casting Tuples and Lists
================

1.Convert List to Tuple
Syntax: tuple(list)
2.Convert Tuple to List
Syntax: list(Tuple)
"""
# List

# Introduction to Lists
"""
====================
List
====================
A Read and Write Collection of Variables that may be used to sort certain data.

Syntax: 
identifier = [value, value1, value2]
courses = ["BSIT", "BSCS", "BSIS"]
"""

# Reading the entire list
"""
====================
Reading Whole List
====================
You can read a list by printing the whole list.

Syntax:
print(list)
"""

# Reading specific items in a list
"""
===================
Reading List Items
===================
You can read a list by printing one of the items inside it by using an index.

Syntax:
print(list[index])
"""

# Explanation of indexing in lists
"""
===================
Index
===================
The number of where an item is in a collection (List).

(+) Positive Index:  0   1   2
(-) Negative Index: -3  -2  -1
Index Diagram: 
    (+) index    0      1      2  
    (-) index   -3     -2     -1
Example:
    courses = ["BSIT", "BSCS", "BSIS"] 
"""

# Reading a range of items in a list
"""
===================
Reading List Range
===================
You can read a list's range of items by specifying a range of indices.

Syntax:
print(list[startIndex:endIndex])
print(list[:endIndex])
print(list[startIndex:])

Note: The `endIndex` item is excluded.
"""

# Modifying items in a list
"""
==================
Assigning List Item
==================
You can assign a list item by using an index and an assignment operator (=).

Syntax:
list[index] = value
Example:
list[0] = "HotDog"
"""

# Getting the number of items in a list
"""
================
List Length
================
You can check the number of items in a list by using the `len` function.

Syntax:
len(list)
"""

# Counting occurrences of an item in a list
"""
================
List Count
================
You can count how many times an item occurs in a list by using the `count()` function.

Syntax:
list.count(value)
"""

# Adding items to the end of a list
"""
===============
Adding Items to List using append()
===============
The `append()` method adds an item at the *end of the list*.

Syntax:
list.append(value)
Example:
list.append("CheeseDog")
"""

# Adding items to the specified index of a list
"""
==============
List ADD ITEMS by INSERT()
==============
insert() adds an item at the SPECIFIED INDEX

Syntax:
list.insert(index,value)
Example:
list.inser(0,"HotDog")

"""

# Removing Items in the List using remove()
"""
================
List DELETE ITEMS by REMOVE()
================
remove() deletes an item based on their value

Syntax:
list.remove(value)
Example:
list.remove("BSIT")
"""

# Removing Items in the List using pop()
"""
=================
List DELETING ITEMS by POP()
=================
pop() deletes an item based on their index but if index is not specified, it deletes the last item

Syntax:
list.pop() which remove the last item
list.pop(index) which remove the specified index on the list
Example:
list.pop(1)
"""

# Removing Items in the List using del
'''
del delete an item based on their index but if index is not specified it deletes the whole list

Syntax
del list[index] which remove an item depends in the index
del list which remove the whole list
Example:
del list[1]
'''

# Clearing a list using clear()
'''
============
Clearing a List
============
clear deletes all the value in a List

Syntax and Example:
list.clear()
'''

# Copying a list using copy()
'''
============
Copying a List
============
copy() copies the whole list which can be assign to a new List

Syntax and Example:
listOne = ["One","Two","Three"]
listTwo = listOne.copy()

'''

# Combining a list
'''
============
Combining a Lists BY ADDING
============
use '+' operator to combine a list

Syntax and Example:
listOne = ["One","Two","Three"]
listTwo = ["Four","Five"]
listThree = listOne + listTwo
'''

# Combining a list using extend()
'''
============
Combining a Lists BY EXTEND()
============
extend() combines lists by appending the specified list to the end of the first list

Syntax and Example:
listOne = ["One","Two","Three"]
listTwo = ["Four","Five"]
listOne.extend(listTwo)
'''

# Reversing a list using reverse()
'''
============
REVERSE List Item
============
reverse() Reverses the order of the List's Items.

Syntax and Example:
list.reverse()
'''

# Sorting List Item using sort()
'''
============
SORT List Item
============
sort() Sort's List's Item by Alphabet or Value depending on Data Type

Syntax and Example:
list.sort() Ascending Order
list.sort(reverse = True) Descending Order
'''

# Nested List
'''
============
Nested List Item
============
A List inside a List also known as Sublist

Syntax and Example:
list = [1,2,3,["one","two"]]
'''

# How to use List

courses = ["BSIT", "BSCS", "BSIS", "BSECE"]
# Reading Whole List

print(courses)
# Reading List Items
print(courses[0])

print("===============")

# Reading List Items using Loop
for data in range(len(courses)):
    print(courses[data])
print("===============")

# Reading List Range
print(courses[1:3])

# Assigning List Item
print("Assign List Item BSIT into HotDog")
# courses[0] = "HotDog"
print(courses)

# List Length
print(len(courses))

# List Count
# courses[1] = "HotDog"
print(courses.count("HotDog"))

# append() Function
print("===============")
print("Adding an Item to the end of the List")
courses.append("IloveyouIT")
courses.append("IhateyouIT")
print(courses)

# insert() Function
print("===============")
print("Adding an Item to the Specied Index of the List")
# ['BSIT', 'BSCS', 'BSIS', 'BSECE', 'EdiWow', 'IloveyouIT', 'IhateyouIT']
courses.insert(4, "EdiWow")
# ['BSIT', 'BSCS', 'BSIS', 'BSECE', 'EdiWow', 'EdiShing', 'IloveyouIT', 'IhateyouIT']
courses.insert(5, "EdiShing")
print(courses)

# remove() Function
print("===============")
print("Removing Items on the List using remove()")
courses.remove("EdiWow")
courses.remove("EdiShing")
courses.remove("IloveyouIT")
courses.remove("IhateyouIT")
print(courses)

# remove() Function
print("===============")
print("Removing Items on the List using pop()")
courses.pop(2)
print(courses)

# del Function

print("===============")
print("Removing Items on the List using del")
del courses[0]
print(courses)

# clear() Function

print("===============")
print("Removing Items on the List using clear()")
courses.clear()
print(courses)

# copy() Function
print("===============")
print("Copying a List using copy()")
listOne = ["One", "Two", "Three"]
listTwo = listOne.copy()
print("List one:", listOne)
print("List two:", listTwo)

# Combining lists
print("===============")
print("Combining two list")
listOne = ["One", "Two", "Three"]
listTwo = ["Four", "Five"]
listThree = listOne + listTwo
print("List one:", listOne)
print("List two:", listTwo)
print("List Three:", listThree)

# Combining lists using extends()
print("===============")
print("Combining two list")
listOne = ["One", "Two", "Three"]
listTwo = ["Four", "Five"]
print("List one:", listOne)
print("List two:", listTwo)
listOne.extend(listTwo)
print("Combined", listOne)

# Reversing lists using reverse()
print("===============")
print("Reversing A list")
listOne.reverse()
print(listOne)

# Sorting lists using using()
print("===============")
print("Sorting A list")
listOne.sort()
print("Not Reverse :", listOne)
listOne.sort(reverse=True)
print("Reversed :", listOne)

# Nested list
print("===============")
print("Nested list")
randomList = [1, 2, 3, [["one", "two"], "three"]]
print(randomList[3])         # [["one","two"],"three"]
print(randomList[3][1])      # "three"
print(randomList[3][0][1])   # "two"
