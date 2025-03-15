import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        self.display_box(
            f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    def take_damage(self, amount):
        self.health -= amount
        self.display_box(
            f"{self.name} takes {amount} damage! Health: {self.health}")

    def display_box(self, message):
        print("+" + "-" * (len(message) + 2) + "+")
        print(f"| {message} |")
        print("+" + "-" * (len(message) + 2) + "+")


class Hero(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)
        self.inventory = []

    def add_loot(self, loot):
        self.inventory.append(loot)
        self.display_box(f"You found: {loot}!")

    def show_inventory(self):
        print("+------- Inventory -------+")
        [print(f"| {item:<24}|") for item in self.inventory] if self.inventory else print(
            "| Empty                  |")
        print("+-------------------------+")


class Slime(Character):
    def __init__(self):
        super().__init__('Slime', 50, 10)
        self.loot = random.choice(['Slime Goo', 'Health Potion'])

    def take_damage(self, amount):
        super().take_damage(amount)
        return self.loot if self.health <= 0 else None
