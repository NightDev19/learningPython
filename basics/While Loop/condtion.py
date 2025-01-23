# print("Crush ka ba niya?")
# while True:
#     answer = input("Yes or No : ")
#     if answer not in ["Yes", 'yes', 'YES', 'y', 'Y']:
#         print("Oo nga, d ka niya gusto")
#         break
#     print('Edi naol')
#     break

#  Even or Odd

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0 #Index
# while i < len(number):
#     if number[i] % 2 != 0:
#         print(f"Odd  : {number[i]}")
#     else:
#         print(f"Even : {number[i]}")
#     i += 1

print("Even Or Odd")
while True:
    put = input("Enter num : ")
    if put.isalpha():
        print("Error")
    elif put == "":
        print("Enter your input")
    elif int(put) % 2 == 0:
        print(f"Even {put}")
    else:
        print(f"Odd : {put}")
