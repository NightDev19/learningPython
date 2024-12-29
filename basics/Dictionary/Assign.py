from dict import student

# assigning a value to a key
student["subjects"] = ["Math", "Science", "English"]
print(student["subjects"]) 

# printing subjects using loop
for i,subject in enumerate(student["subjects"],1):
    print(f"{i}.{subject}")