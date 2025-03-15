'''
TODO: Make an RPG Shop Management using all the basics Arrays


Requirement:
Arrays : Sets / List / Tuples / Dict

use a simple logic to it using IO 

Simple Logic to locate information in Dictionary
    money -= shop["potion"]["price"]
    print(money)
'''

money = 1000
# Dict of Items in shop
shop = {
    "sword": {
        "price": 100,
        "desc": "something sharp"
    },
    "shield": {
        "price": 100,
        "desc": "something Defensive"
    },
    "potion": {
        "price": 50,
        "desc": "something comfortable"
    },

}


'''
Automatic numbering while printing the key of the Dictionary
'''

for i, key in enumerate(shop, start=1):
    print(f"{i}.){key} - ${shop[key]["price"]}\nDescription : {shop[key]["desc"]}")

while True:
    print(f"Your Balance : {money}")
    choice = input(f"\nWant to buy something? : (1-{len(shop)} or 'q' to quit): ")

    # Validate Choices
    if choice.lower() == 'q':
        print("Good bye!")
        break
    elif choice.isdigit() and 1 <= int(choice) <= len(shop): 
        # Chosen Item Explanation
        '''
         * chosenItem
         ``
            - Casting it into a list and took the Keys only to create ["Sword","Shield","Potion"]
            - using that it can automatically select the index but the index is starting to zero but the numbering is start at one 
            - so we make the choice into a number and less it to 1
            
            Example :
            
            index    0        1        2
            shop ["Sword","Shield","Potion"]
            num      1        2        3
            
            and the choice input is 1 since the num is 1 but the index is zero so 
            we less it in 1 to take the index into 0 so we can choose the "sword"
        '''
        chosenItem = list(shop.keys())[int(choice) - 1] 
        print(f"You chose the {chosenItem} to buy.") # Sample
        #Check Money affordability
        if money >= shop[chosenItem]["price"]:
            money -= shop[chosenItem]["price"]
            print(f"You've bought {chosenItem}. Balance: ${money}")
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Choice: Please Try Again!")
    
