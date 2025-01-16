"""====================================[AND Operator]========================================"""

# age = int(input("Enter your age: "))
# height = int(input("Enter your height: "))

# if age >= 18 and height >= 176:
#     print("Legal age and tall")
# elif age >= 18 and  height >= 150:
#     print("Legal age but average")
# elif age >= 18:
#     print("Legal age but short")
# else:
#     print("Underage")
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username == "night" and password == "admin":
#     print(f"Login successful\nWelcome {username}")
# elif username == "Dev" and password == "admin123":
#     print(f"Login successful\nWelcome {username}")
# else:
#     print("Invalid username or password")
   
"""====================================[OR Operator]========================================"""

# Teacher said you need to bring a meter stick or a ruler and water to class
hasMeterStick = False
hasRuler = True
hasWater = True

if hasMeterStick and hasWater or hasRuler and hasWater:
    print("You can enter the class")
else:
    print("You can't enter the class")