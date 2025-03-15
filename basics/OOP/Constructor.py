#Create a class named Character
class Character:
    def __init__(self,name,hp,mp,attack,lv): #Initializes the attributes of the class
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.lv = lv
        print(f"{self.name}!, Your Character Created")
        
char1 = Character("Night",100,50,12,1)
print(vars(char1))
char2 = Character("Day",100,50,12,1)
print(vars(char2))
#Accessing the attributes of the object
