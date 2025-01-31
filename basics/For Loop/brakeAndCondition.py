# basket = ["Apple", "Banana", "Cherry"]

# for fruit in basket:
#     print(f"I ate the {fruit}")
#     if fruit == "Banana":
#         break

numbers = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
        continue #Skip one tick or step in the loop
    print(f"{number} is odd")