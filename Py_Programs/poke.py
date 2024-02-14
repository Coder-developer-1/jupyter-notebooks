import requests

while True:

 pokemon = input("Tell me , Which pokemon character are you finding ?  ")
 pokemon = pokemon.lower()

 url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

 req = requests.get(url)

 if req.status_code == 200:
    data =req.json()

    print(f"Name is = {data['name']}")
    print("Abilitis are =")
    for ability in data['abilities']:
     print(ability['ability']['name'])

 else:
    print("Sorry , Pokemon didn't found")    