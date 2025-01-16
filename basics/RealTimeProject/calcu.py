op = ["+", "-", "*", "/"]

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
print(f"==== Choose Operator ====\n1.) {op[0]}\n2.) {op[1]}\n3.) {op[2]}\n4.) {op[3]}\n")
ops = int(input("Choose one (1-4): ")) - 1  # Subtracting 1 to match index

if 0 <= ops < len(op):
    chosen_op = op[ops]
    print(f"You've chosen {chosen_op}")
    
    # Perform the operation based on the chosen operator
    if chosen_op == "+":
        print(f"{num1} {chosen_op} {num2} = {num1 + num2}")
    elif chosen_op == "-":
        print(f"{num1} {chosen_op} {num2} = {num1 - num2}")
    elif chosen_op == "*":
        print(f"{num1} {chosen_op} {num2} = {num1 * num2}")
    elif chosen_op == "/":
        if num2 != 0:
            print(f"{num1} {chosen_op} {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator choice. Please choose a number between 1 and 4.")
