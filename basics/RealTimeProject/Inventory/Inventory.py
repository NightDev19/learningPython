import sqlite3
import datetime


class Inventory:
    def __init__(self):
        """Initialize database and create tables if they don't exist."""
        self.conn = sqlite3.connect("inventory.db")
        self.cursor = self.conn.cursor()

        # Create inventory table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                price INTEGER,
                quantity INTEGER
            )
        """)

        # Create history table with total_price for tracking sales revenue
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action TEXT,
                item_id INTEGER,
                item_name TEXT,
                quantity INTEGER,
                price INTEGER,
                total_price INTEGER, 
                timestamp TEXT,
                FOREIGN KEY (item_id) REFERENCES inventory(id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()

    def log_history(self, action, item_name, quantity=None, price=None):
        """Log actions in the history table."""
        self.cursor.execute(
            "SELECT id FROM inventory WHERE name=?", (item_name,))
        item = self.cursor.fetchone()
        item_id = item[0] if item else None

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Calculate total price for sales transactions
        total_price = price * quantity if action == "Sold" and price and quantity else None

        self.cursor.execute("""
            INSERT INTO history (action, item_id, item_name, quantity, price, total_price, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (action, item_id, item_name, quantity, price, total_price, timestamp))
        self.conn.commit()

    def add(self, **kwargs):
        """Add an item to inventory and log the action."""
        try:
            self.cursor.execute(
                "INSERT INTO inventory (name, price, quantity) VALUES (:name, :price, :quantity)", kwargs)
            self.conn.commit()
            self.log_history(
                "Added", kwargs['name'], kwargs['quantity'], kwargs['price'])
            print(f"{kwargs['name']} added to inventory.")
        except sqlite3.IntegrityError:
            print(f"Error: {kwargs['name']} already exists.")

    def edit(self, item_name):
        """Edit item price or quantity and log the action."""
        self.cursor.execute(
            "SELECT * FROM inventory WHERE name=?", (item_name,))
        item = self.cursor.fetchone()

        if not item:
            return print(f"{item_name} not found.")

        updates = {}

        new_price = input(f"New price for {item_name} (Enter to skip): ")
        new_quantity = input(f"New quantity for {item_name} (Enter to skip): ")

        if new_price:
            updates["price"] = int(new_price)
        if new_quantity:
            updates["quantity"] = int(new_quantity)

        if updates:
            set_clause = ", ".join(f"{col}=?" for col in updates.keys())
            self.cursor.execute(
                f"UPDATE inventory SET {set_clause} WHERE name=?", (*updates.values(), item_name))
            self.conn.commit()

            # Log changes in history
            if "price" in updates:
                self.log_history("Price Edited", item_name,
                                 price=updates["price"])
            if "quantity" in updates:
                self.log_history("Quantity Edited", item_name,
                                 quantity=updates["quantity"])

            print(f"{item_name} updated.")
        else:
            print("No changes made.")

    def remove(self, item_name):
        """Remove an item from inventory and log the action."""
        self.cursor.execute(
            "SELECT id FROM inventory WHERE name=?", (item_name,))
        item = self.cursor.fetchone()

        if not item:
            return print(f"Error: {item_name} not found in inventory.")

        # Remove the item
        self.cursor.execute("DELETE FROM inventory WHERE name=?", (item_name,))
        self.conn.commit()

        # Log removal action
        self.log_history("Removed", item_name)
        print(f"{item_name} removed successfully.")

    def sell(self, item_name, quantity):
        """Sell an item, update inventory, and log the action."""
        self.cursor.execute(
            "SELECT * FROM inventory WHERE name=?", (item_name,))
        if not (item := self.cursor.fetchone()):
            return print(f"{item_name} not found.")

        if item[3] < quantity:
            return print(f"Not enough stock. Available: {item[3]}")

        new_qty = item[3] - quantity
        if new_qty:
            self.cursor.execute(
                "UPDATE inventory SET quantity=? WHERE name=?", (new_qty, item_name))
        else:
            self.remove(item_name)

        self.conn.commit()
        total_price = item[2] * quantity  # price * quantity
        self.log_history("Sold", item_name, quantity, item[2])
        print(f"Sold {quantity} {item_name}(s) for ${total_price}")
        input()

    def view_history(self):
        """Display history of transactions with total price for sales."""
        self.cursor.execute("SELECT * FROM history ORDER BY timestamp DESC")
        history = self.cursor.fetchall()
        if not history:
            return print("No history available.")

        print("\nTransaction History:\n" + "-" * 70)
        print(
            f"{'No.':<5} {'Action':<10} {'Item':<15} {'Qty':<8} {'Price':<8} {'Total':<10} {'Timestamp':<20}")
        for i, (id, action, item_id, name, qty, price, total_price, timestamp) in enumerate(history, 1):
            print(
                f"{i:<5} {action:<10} {name:<15} {qty if qty else '-':<8} {price if price else '-':<8} {total_price if total_price else '-':<10} {timestamp:<20}")
        print("-" * 70)

    def display(self):
        """Display inventory in a well-formatted table."""
        self.cursor.execute("SELECT * FROM inventory")
        items = self.cursor.fetchall()

        if not items:
            return print("Inventory is empty.")

        print("\nInventory List:\n" + "-" * 50)
        print(f"{'No.':<5} {'Name':<20} {'Price':<10} {'Quantity':<10}")
        print("-" * 50)

        for i, (id, name, price, qty) in enumerate(items, 1):
            print(f"{i:<5} {name:<20} {price:<10} {qty:<10}")

        print("-" * 50)

    def __del__(self):
        """Close database connection."""
        self.conn.close()
        print("Inventory closed.")
