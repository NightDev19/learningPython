operator = ["+", "-", "*", "/"]

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
print(f"==== Choose Operator ====\n1.) {operator[0]}\n2.) {
      operator[1]}\n3.) {operator[2]}\n4.) {operator[3]}\n")
choice = int(input("Choose one (1-4): "))  # Subtracting 1 to match index

if 1 <= choice <= 4:
    if operator[choice - 1] == "/" and num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"You've chosen {operator[choice - 1]}")
        print(eval(f"{num1} {operator[choice - 1]} {num2}"))
else:
    print("Invalid choice. Please select a valid operator.")
