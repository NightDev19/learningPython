class POS:
    def __init__(self):
        self.items = set()
        self.transactions = []

    def addItem(self,item):
        self.items.add(item)
        print(f"Added: {item}")

    def removeItem(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed: {item}")
        else:
            print(f"Not Found: {item}")

    def transaction(self,item,action):
        self.transactions.append((item,action))

    def display(self):
        print("[===POS Items===]")
        for item in self.items:
            print(item)

    def displayTransactions(self):
        print("[===Transactions===]")
        for transaction in self.transactions:
            print(f"{transaction[1]}: {transaction[0]}")

if __name__ == "__main__":
    pos = POS()
    while True:
        print("\n1.Add Item\n2.Remove Item\n3.Display\n4.Display Transactions\n5.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter the item: ")
            pos.addItem(item)
            pos.transaction(item,"Added")
        elif choice == "2":
            item = input("Enter the item: ")
            pos.removeItem(item)
        elif choice == "3":
            pos.transaction(item,"Removed")
            pos.transaction(item, "Added")
        elif choice == "4":
            print("Exiting...")
            pos.displayTransactions()
        elif choice == "5":
            break
        else:
            print("Invalid Choice!")

