'''
* RPG Inventory management System using Dict
    - Two dict [invetory and shop]
    
    [===Functionality===]
        - addItem()
        - removeItem()
        - buyItem()
        - sellItem()
        - display_inventory()
        - display_shop()
        - checkAvail()
'''

# Variables
inventory = {
    #      Key  :          Value
    #          key :   value   key :  value
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


def display_shop():
    print('[===Shop===]')
    for i, (key, value) in enumerate(shop.items(), start=1):
        print(f"{i}.){key} : ${value["price"]}\n -{value['desc']}")


def buy_items(item_name, quantity):
    global balance
    price = shop[item_name]['price']
    total_cost = price * quantity
    if balance >= total_cost:
        if item_name in inventory:
            inventory[item_name]['quantity'] += quantity
        else:
            inventory[item_name] = {'quantity': quantity, 'price': price}
        balance -= total_cost
        transactionHistory.append(
            f"Bought {quantity} {item_name} for ${total_cost}")
        print(f"Bought {quantity} {item_name} for ${total_cost}")
    else:
        print("Not enough balance")


def sell_items(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name]['quantity'] >= quantity:
            inventory[item_name]['quantity'] -= quantity
            transactionHistory.append(f"Sold {quantity} {item_name}(s)")
            print(f"Sold {quantity} {item_name}(s)")
        else:
            print("Item not Found!")


def display_inventory():
    print('[===Inventory===]')
    for i, (item, details) in enumerate(inventory.items(), start=1):
        print(f"{i}.) {item} : {details['quantity']} units")


def display_transaction_history():
    print("[===[Transaction History]===]")
    for i, details in enumerate(transactionHistory, start=1):
        print(f"{i}.){details}")


while True:
    clear()
    print("[===Welcome to Shop===]")
    print("\n[===OPTIONS===]\n1. View Shop\n2. Buy Item\n3. Sell Item\n4. View Inventory\n5. View Transaction\n6. Check Balance\n7. Quit")
    choice = int(input("Choose an Option: "))
    if choice == 1:
        clear()
        display_shop()
        input()
    elif choice == 2:
        clear()
        YN = input("Do You want to buy ?(y/n) :")
        if YN.lower() == 'y':
            display_shop()
            while True:
                item_name = input("Enter the item you want to buy: ").lower()
                quantity = input("Enter the quantity: ")
                if item_name and quantity != "":
                    buy_items(item_name, int(quantity))
                    break
                else:
                    print("Put the item name or how many item will you sell!")
    elif choice == 3:
        clear()
        YN = input("Do You want to sell ?(y/n) :")
        if YN.lower() == 'y':
            display_inventory()
            while True:
                item_name = input("Enter the item you want to sell: ").lower()
                quantity = input("Enter the quantity: ")
                if item_name != "" and quantity != "":
                    sell_items(item_name, int(quantity))
                    break
                else:
                    print("Put the item name or how many item will you sell!")
    elif choice == 4:
        clear()
        display_inventory()
        input()
    elif choice == 5:
        clear()
        display_transaction_history()
        input()
    elif choice == 6:
        clear()
        print(f"Balance : {balance}")
        input()
    elif choice == 7:
        clear()
        print("Goodbye!")
        break
    else:
        print("Invalid Option. Please try again.")
        input()
