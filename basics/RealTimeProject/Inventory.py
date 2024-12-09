'''
* RPG Inventory management System using Dict
    - Two dict [invetory and shop]
    
    [===Functionality===]
        - addItem()
        - removeItem()
        - buyItem()
        - sellItem()
        - displayInventory()
        - displayShop()
        - checkAvail()
'''

# Variables
inventory = {
    "sword": {"quantity": 10, "price": 100},
    "shield": {"quantity": 10, "price": 150},
    "wand": {"quantity": 10, "price": 100},
    "potion": {"quantity": 10, "price": 50},
}
shop = {
    "potion": {"price": 50, "desc": "Healing Potion"},
    "wand": {"price": 100, "desc": "Magic Wand"},
    "sword": {"price": 100, "desc": "Something Sharp"},
    "shield": {"price": 100, "desc": "Something Defensive"},
}
transactionHistory = []
uniqueItems = set()
balance = 1000

# Function


def clear():
    import os
    os.system('cls')


def displayShop():
    print('[===Shop===]')
    for i, (items, details) in enumerate(shop.items(), start=1):
        print(f"{i}.){items} : ${details["price"]}\n -{details['desc']}")


def buyItems(itemName, quantity):
    global balance
    price = shop[itemName]['price']
    totalCost = price * quantity
    if balance >= totalCost:
        if itemName in inventory:
            inventory[itemName]['quantity'] += quantity
        else:
            inventory[itemName] = {'quantity': quantity, 'price': price}
        balance -= totalCost
        transactionHistory.append(
            f"Bought {quantity} {itemName} for ${totalCost}")
        print(f"Bought {quantity} {itemName} for ${totalCost}")
    else:
        print("Not enough balance")


def sellItems(itemName, quantity):
    if itemName in inventory:
        if inventory[itemName]['quantity'] >= quantity:
            inventory[itemName]['quantity'] -= quantity
            transactionHistory.append(f"Sold {quantity} {itemName}(s)")
            print(f"Sold {quantity} {itemName}(s)")
        else:
            print("Item not Found!")


def displayInventory():
    print('[===Inventory===]')
    for i, (item, details) in enumerate(inventory.items(), start=1):
        print(f"{i}.) {item} : {details['quantity']} units")


def displayTransactionHistory():
    print("[===[Transaction History]===]")
    for i, details in enumerate(transactionHistory, start=1):
        print(f"{i}.){details}")


while True:
    print("[===Welcome to Shop===]")
    print("\n[===OPTIONS===]\n1. View Shop\n2. Buy Item\n3. Sell Item\n4. View Inventory\n5. View Transaction\n6. Check Balance\n7. Quit")
    choice = int(input("Choose an Option: "))
    if choice == 1:
        clear()
        displayShop()
    elif choice == 2:
        clear()
        YN = input("Do You want to buy ?(y/n) :")
        if YN.lower() == 'y':
            displayShop()
            itemName = input("Enter the item you want to buy: ").lower()
            quantity = int(input("Enter the quantity: "))
            buyItems(itemName, quantity)
    elif choice == 3:
        clear()
        YN = input("Do You want to sell ?(y/n) :")
        if YN.lower() == 'y':
            displayShop()
            itemName = input("Enter the item you want to sell: ").lower()
            quantity = int(input("Enter the quantity: "))
            sellItems(itemName, quantity)
    elif choice == 4:
        clear()
        displayInventory()
    elif choice == 5:
        clear()
        displayTransactionHistory()
    elif choice == 6:
        clear()
        print(f"Balance : {balance}")
    elif choice == 7:
        clear()
        print("Goodbye!")
        break
    else:
        print("Invalid Option. Please try again.")
