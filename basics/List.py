
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
