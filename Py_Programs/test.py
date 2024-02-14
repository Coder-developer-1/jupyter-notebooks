import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    while True:
        pokemon_name = input("Which Pokemon do you want to find? (Type 'exit' to quit): ").lower()

        if pokemon_name == 'exit':
            print("Exiting the Pokemon Finder. Goodbye!")
            break

        pokemon_data = get_pokemon_data(pokemon_name)

        if pokemon_data:
            abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
            moves = [move['move']['name'] for move in pokemon_data['moves']]
            held_items = [item['item']['name'] for item in pokemon_data['held_items']]

            print(f"\nPokemon: {pokemon_data['name'].capitalize()}")
            print(f"Height: {pokemon_data['height']} decimetres")  # Height in decimetres
            print("Abilities:")
            for ability in abilities:
                print(f"  - {ability.capitalize()}")

            print("Held Items:")
            for item in held_items:
                print(f"  - {item.capitalize()}")
        else:
            print(f"Pokemon '{pokemon_name}' not found. Please check the spelling and try again.")

if __name__ == "__main__":
    main()
