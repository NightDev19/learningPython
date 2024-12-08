print("Welcome to my Calculator")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
operator = input("Enter the operator (+ | - | * | / | % | ** | //): ")

if operator in ["+", "-", "*", "**"]:
    result = eval(f"{num1} {operator} {num2}")
elif operator == "/" and num2 != 0:
    result = num1 / num2
elif operator == "%" and num2 != 0:
    result = num1 % num2
elif operator == "//" and num2 != 0:
    result = num1 // num2
else:
    result = "Error: Invalid operation or division by zero"

# Convert to int if the result is a whole number
if isinstance(result, float) and result.is_integer():
    result = int(result)

print(f"The result is: {result}")
