import json

def delete_user(user_list):
    name = input("Name des Mitglieds, das gelöscht werden soll: ")
    
    for user in user_list:
        if user["name"] == name:
            user_list.remove(user)
            
            try:
                with open("users.json", "w", encoding="utf-8") as file:
                    json.dump(user_list, file, indent=4, ensure_ascii=False)
                print("Mitglied gelöscht")
            except:
                print("Fehler beim Löschen des Mitglieds.")
                print("Kehre zurück ins Hauptmenü..")
            
            return user_list
    
    print("Mitglied nicht gefunden.")
    print("Kehre zurück ins Hauptmenü..")
    return user_list