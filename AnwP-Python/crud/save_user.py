import json


def add_user(user_list):
    name = input("Name: ")
    age = input("Alter: ")
    email = input("Email: ")
    hobby = input("Hobby: ")
    
    user = {
        "name": name,
        "alter": age,
        "email": email,
        "hobby": hobby
    }
    
    if name in [user["name"] for user in user_list]:
        print("Mitglied bereits vorhanden und kann nicht hinzugefügt werden.")
        print("Kehre zurück ins Hauptmenü..")
        return user_list
    
    user_list.append(user)
    
    try:
        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(user_list, file, indent=4, ensure_ascii=False)
        print("Mitglied hinzugefügt")
    except:
        print("Fehler beim Hinzufügen des Mitglieds.")
        print("Kehre zurück ins Hauptmenü..")
    
    return user_list