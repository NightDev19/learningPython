'''
Example List

username = ["John","Alenere","David"]

password = ["abc123","123abc","hahatdog"]

PS the password and username are paired by index

John’s Password is abc123

Then make the user input a username and password then check if the input matches the pair of username and password

if account exists display “Welcome , [username]”

if not “Account not found”
'''


username = ["John","Alenere","David"]
password = ["abc123","123abc","hahatdog"]
chances = 3



while chances > 0:
    print(f"Chances left: {chances}")
    user = input("Enter your username: ")
    passw = input("Enter your password: ")
    for i in range(len(username)):
        if username[i] == user and password[i] == passw:
            print(f"Welcome {username[i]}")
            break
        else:
            print("Account not found")
            chances -= 1
            break
