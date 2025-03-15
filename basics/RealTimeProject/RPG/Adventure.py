import os
import random
from Character import Hero, Slime


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_actions():
    print("+-------------------------+")
    print("| 1. Attack  2. Run       |")
    print("| 3. Inventory            |")
    print("+-------------------------+")


def start_game():
    hero = Hero(input("Enter your hero's name: "))
    print(f"Welcome, {hero.name}!")

    while hero.health > 0:
        print("+----------------------------+")
        print("| 1. Adventure 2. Inventory  |")
        print("+----------------------------+")
        action = input("Choose: ").strip()
        clear_screen()

        if action == '2':
            hero.show_inventory()
            continue

        if random.choice([True, False]):
            if random.choice([True, False]):
                slime = Slime()
                print(f"A wild {slime.name} appears!")

                while hero.health > 0 and slime.health > 0:
                    show_actions()
                    action = input("Choose: ").strip()
                    clear_screen()

                    if action == '1':
                        loot = slime.take_damage(
                            random.randint(1, hero.attack_power))
                        if loot:
                            hero.add_loot(loot)
                        if slime.health > 0:
                            slime.attack(hero)
                    elif action == '2':
                        print("You run away!")
                        break
                    elif action == '3':
                        hero.show_inventory()
            else:
                print("You sense something but nothing happens...")

        else:
            print("You find nothing...")

        if input("Continue? (yes/no): ").strip().lower() != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    start_game()
