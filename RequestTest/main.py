import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ded4239272a84ca88b7547a5409097b1'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "generate",
    "photo_id": -1
}

body_switch_name = {
    "pokemon_id": "144275",
    "name": "generate",
    "photo_id": -1
}

body_add_pokeball = {
    "pokemon_id": "144275"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_switch_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_switch_name)
print(response_switch_name.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)