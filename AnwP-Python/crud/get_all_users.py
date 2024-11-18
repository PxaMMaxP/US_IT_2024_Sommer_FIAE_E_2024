import json

def get_all_users():
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            users = json.load(file)
    except:
        print("Fehler beim Lesen der 'users.json' Datei.")
        users = []
        
    return users