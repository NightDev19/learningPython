from Inventory import Inventory
import os


def main():
    inventory = Inventory()
    menu = {
        "1": ("Add Item", lambda: inventory.add(
            name=input("Enter item name: "),
            price=int(input("Enter item price: ")),
            quantity=int(input("Enter item quantity: "))
        )),
        "2": ("Edit Item", lambda: inventory.edit(input("Enter item name to edit: "))),
        "3": ("Remove Item", lambda: inventory.remove(input("Enter item name to remove: "))),
        "4": ("Sell Item", lambda: inventory.sell(
            input("Enter item name to sell: "),
            int(input("Enter quantity to sell: "))
        )),
        "5": ("View Inventory", inventory.display),
        "6": ("View History", inventory.view_history),  # Added option
        "7": ("Exit", exit)
    }

    while True:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("\n--- Inventory Management ---")
        for key, (desc, _) in menu.items():
            print(f"{key}. {desc}")

        action = menu.get(input("Enter your choice: "),
                          (None, lambda: print("Invalid choice, try again!")))[1]
        action()
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
