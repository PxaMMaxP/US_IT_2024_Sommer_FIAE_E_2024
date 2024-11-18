from get_all_users import get_all_users
from save_user import add_user
from update_user import update_user
from delete_user import delete_user

if __name__ == "__main__":
    users = get_all_users()
    
    print("Hauptmenü:")
    
    while True:
        print("1: Mitglieder Liste lesen")
        print("2: Mitglied hinzufügen")
        print("3: Mitglied bearbeiten")
        print("4: Mitglied entfernen")
        print("5: Programm beenden")
        
        auswahl = input("Bitte wählen Sie eine Option: ")
        
        if auswahl == "1":
            print("\nMitglieder Liste lesen..\n")
            print("Mitglieder:")
            for user in users:
                print(f"Name: {user['name']}, Alter: {user['alter']}, Email: {user['email']},")
                print(f"    Hobby: {user['hobby']}")
        elif auswahl == "2":
            print("\nMitglied hinzufügen..\n")
            users = add_user(users)
        elif auswahl == "3":
            print("\nMitglied bearbeiten..\n")
            users = update_user(users)
        elif auswahl == "4":
            print("\nMitglied entfernen..\n")
            users = delete_user(users)
        elif auswahl == "5":
            exit(0)
        else:
            print("Ungültige Eingabe")
            
        print()