import requests

# Function to fetch Pokémon data with a callback
def fetch_pokemon(name, callback):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        callback(data)  # Call the callback function with fetched data
    else:
        print("Character not found")

# Lambda function as a callback to process and print the data
process_pokemon = lambda data: (
    print(f"Name: {data['name']}\nAbilities:"),
    print(data['abilities']['ability']['name']) ,
    
)

# Get user input
userInput = input("Enter Poke Character: ").strip().lower()

# Call fetch_pokemon with the callback
fetch_pokemon(userInput, process_pokemon)
