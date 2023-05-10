import mysql.connector

def insert_pokemon(pokemon):
    print(f"Inserindo pokemon: {pokemon['Name']}")
    conn = mysql.connector.connect(
        host='localhost',
        user='blablabla',
        database='blablablabla'
    )
    c = conn.cursor()
    c.execute("INSERT INTO pokemon (Name, Types, BaseStats, GrowthRate, GenderRatio, BaseExp, CatchRate, Happiness, Abilities, HiddenAbilities, Moves, TutorMoves, EggMoves, EggGroups, HatchSteps, Height, Weight, Color, Shape, Habitat, Category, Pokedex, Generation, Evolutions) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
              (pokemon['Name'], pokemon['Types'], pokemon['BaseStats'], pokemon['GrowthRate'],
               pokemon['GenderRatio'], pokemon.get('BaseExp', 0), pokemon['CatchRate'], pokemon.get('Happiness', 0),
               pokemon['Abilities'], pokemon.get('HiddenAbilities', ''), pokemon['Moves'],
               pokemon.get('TutorMoves', ''),
               pokemon.get('EggMoves', ''),
               pokemon['EggGroups'], pokemon['HatchSteps'], pokemon['Height'],
               pokemon['Weight'], pokemon['Color'], pokemon['Shape'], pokemon.get('Habitat', ''),
               pokemon['Category'], pokemon['Pokedex'], pokemon.get('Generation', 0), pokemon.get('Evolutions', '')))
    conn.commit()
    conn.close()

def parse_pokemon_data(file_name):
    #print(f"Lendo arquivo: {file_name}")
    with open(file_name, 'r') as file:
        lines = file.readlines()
        current_pokemon = {}
        for line in lines:
            if line.startswith('['):
                if current_pokemon:
                    insert_pokemon(current_pokemon)
                current_pokemon = {}
            elif line.startswith('#'):
                continue
            elif ' = ' in line:
                parts = line.strip().split(' = ')
                if len(parts) == 2:
                    key,value = parts
                    current_pokemon[key] = value
        if current_pokemon:
            insert_pokemon(current_pokemon)

print("Iniciando PBStoSQL.py")
parse_pokemon_data('pokemon.txt')
print("Terminando PBStoSQL.py")
