"""
Author: [sahil kumar singh]
Assignment / Part: HW8 - Q2 and 3  (Dictionaries, I Choose You!and Gotta Archive 'Em All)
Date due: 2022-11-17, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


def create_entry(number,name,type_1,type_2,health_points,attack,defense,speed,is_legendary):
    pokemon={}
    pokemon["Number"]= number
    pokemon["Name"]= name
    if type_2=="":
        type_2= None
    pokemon["Type"]=(type_1,type_2)
    pokemon["Battle stats"]= {}
    pokemon["Battle stats"]["HP"]=health_points
    pokemon["Battle stats"]["Attack"]=attack
    pokemon["Battle stats"]["Defense"]=defense
    pokemon["Battle stats"]["Speed"]=speed
    pokemon["Legendary"]= is_legendary
    return pokemon

def main():
    a_random_pokemon = create_entry(81, "Magnemite", "Electric", "Steel", 25, 35, 70, 95,False)
   
    for key in a_random_pokemon.keys():
        print(f"{key}: {a_random_pokemon[key]}")

main()

def create_pokedex(POKEMON_DATA):
    pokedex={}
    x=POKEMON_DATA.split("\n")
    for name in x:
        nam=name.split(',')
        pokedex.update({nam[1]:create_entry(nam[0],nam[1],nam[2],nam[3],nam[4],nam[5],nam[6],nam[7],nam[8])})
    return pokedex

def main():
    pokedex = create_pokedex(POKEMON_DATA)
    pokemon_key = "Ivysaur"
    if pokemon_key not in pokedex:
        print(f"ERROR: Pokemon {pokemon_key} does not exist!")
    else:
        print(f"PRINTING {pokemon_key}'S INFORMATION...")
        for key in my_favorite_pokemon.keys():
            print(f"{key}: {my_favorite_pokemon[key]}")
 
main()
     
