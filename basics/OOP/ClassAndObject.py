#Creating a Class with some attributes/blueprints for the object
class Character:
    name = ""
    hp = 100
    mp = 50
    attack = 12
    lv = 1 
    
#Creating an object of the class
character1 = Character()
character2 = Character()
print(character1)
print(character2)

#Accessing the attributes of the object
character1.name = "Night"
character2.name = "Day"
print(character1.name)
print(character2.name)