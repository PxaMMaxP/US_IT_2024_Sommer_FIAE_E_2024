import json


def update_user(user_list):
    name = input("Name des Mitglieds, das bearbeitet werden soll: ")
    
    for user in user_list:
        if user["name"] == name:
            print("Mitglied gefunden.")
            print("Folgende Werte können bearbeitet werden:")
            print("1: Name")
            print("2: Alter")
            print("3: Email")
            print("4: Hobby")
            
            auswahl = input("Bitte wählen Sie eine Option: ")
            
            if auswahl == "1":
                new_name = input("Neuer Name: ")
                user["name"] = new_name
            elif auswahl == "2":
                new_age = input("Neues Alter: ")
                user["alter"] = new_age
            elif auswahl == "3":
                new_email = input("Neue Email: ")
                user["email"] = new_email
            elif auswahl == "4":
                new_hobby = input("Neues Hobby: ")
                user["hobby"] = new_hobby
            else:
                print("Ungültige Eingabe")
                print("Kehre zurück ins Hauptmenü..")
                return user_list
            
            try:
                with open("users.json", "w", encoding="utf-8") as file:
                    json.dump(user_list, file, indent=4, ensure_ascii=False)
                print("Mitglied aktualisiert")
            except:
                print("Fehler beim Aktualisieren des Mitglieds.")
                print("Kehre zurück ins Hauptmenü..")
            
            return user_list
    
    print("Mitglied nicht gefunden.")
    print("Kehre zurück ins Hauptmenü..")
    return user_list