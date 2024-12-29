from dict import *
# Two types of reading a Dictionary
# 1. Reading the whole Dictionary
print(StudentOne)
print(StudentTwo)

# 2. Reading Dictionary Items
print(f"Name: {StudentOne['Name']}")
print(f"Age: {StudentOne['Age']}")
print(f"Course: {StudentOne['Course']}")

print(f"Name: {StudentTwo['Name']}")
print(f"Age: {StudentTwo['Age']}")
print(f"Course: {StudentTwo['Course']}")

# using loop to read all items in a Dictionary
for i, (key, value) in enumerate(StudentOne.items(), start=1):
    print(f"{i}.) {key}: {value}")
