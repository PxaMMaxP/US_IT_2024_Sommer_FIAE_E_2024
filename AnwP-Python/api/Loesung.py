import json
import datetime
import random
import urllib.request
import json

CHAR_RACE_URL = "https://www.dnd5eapi.co/api/races"
CHAR_CLASS_URL = "https://www.dnd5eapi.co/api/classes"

def get_races():
    try:
        with urllib.request.urlopen(CHAR_RACE_URL) as response:
            if response.getcode() != 200:
                print("Error: Could not fetch data from API. Status code: ", response.getcode())
                exit(-1)
                
            data = json.loads(response.read().decode())["results"]
            return data
    except Exception as e:
        print(f"Error: {e}")
        exit(-1)
    

def get_classes():
    try:
        with urllib.request.urlopen(CHAR_CLASS_URL) as response:
            if response.getcode() != 200:
                print("Error: Could not fetch data from API. Status code: ", response.getcode())
                exit(-1)
                
            data = json.loads(response.read().decode())["results"]
            return data
    except Exception as e:
        print(f"Error: {e}")
        exit(-1)

def generate_character():
    character = {}
    races = get_races()
    classes = get_classes()

    selected_race_index = random.randint(0, races.__len__()-1)
    selected_class_index = random.randint(0, classes.__len__()-1)
    
    selected_race = races[selected_race_index]
    selected_class = classes[selected_class_index]
    
    character = {
        "race": selected_race['name'],
        "class": selected_class['name'],
    }
    
    return character

def generate_attributes():
    attributes = {}
    
    attributes["strength"] = random.randint(1, 50)
    attributes["intelligence"] = random.randint(1, 50)
    attributes["agility"] = random.randint(1, 50)
    
    return attributes

def generate_character_list():
    characters = []
    
    for i in range(0, 5):
        character = {}
        character['created_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        character.update(generate_character())
        character["attributes"] = generate_attributes()
        characters.append(character)
        
    return characters

def save_character(character):
    with open("characters.json", "w") as file:
        json.dump(character, file, indent=4)
        

if __name__ == "__main__":
    characters = generate_character_list()
    save_character(characters)
    print("Character saved!")