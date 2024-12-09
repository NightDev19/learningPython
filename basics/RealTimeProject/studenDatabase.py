'''
* Goal 
    - Making a Student Database where we can store name of the student using List and Set
    
[===Funtionality===]
    - We can add
    - Delete
    - Display
    - and Checking if there's a Duplicate Student

'''


studentList = []
studentSet = set()

# Add Student
def addStudent(name):
    if name not in studentSet:
        studentList.append(name)
        studentSet.add(name)
        print(f"Added:{name}")
    else:
        print(f"Duplicated:{name}")

# Delete Student
def removeStudent(name):
    if name in studentSet:
        studentList.remove(name)
        studentSet.remove(name)
        print(f"Removed:{name}")


# Display Student
def display():
    print("[===Student List===]")
    studentList.sort()
    for i,data in enumerate(range(len(studentList)),start=1):
        print(f"{i}.){studentList[data]}")
        
# Duplicate Verification
def duplicate(name):
    return name in studentList

addStudent("Sherwin")
addStudent("Sherwin")
addStudent("Angel")
addStudent("Riven")
addStudent("Lam")
addStudent("Lam")
print(studentList)
print(studentSet)
display()
print(duplicate("Lam"))
