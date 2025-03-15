import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} has {self.health} health remaining.\n")

    def is_alive(self):
        return self.health > 0


# Battle simulation
hero = Character("Knight", 30, 8)
slime = Character("Green Slime", 20, 4)

while hero.is_alive() and slime.is_alive():
    hero.attack(slime)
    if slime.is_alive():
        slime.attack(hero)

if hero.is_alive():
    print(f"{hero.name} wins!")
else:
    print(f"{slime.name} wins!")
