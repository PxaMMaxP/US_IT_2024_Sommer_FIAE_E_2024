# Aufgabe 9
# Schreibe ein Programm, das eine einfache Benutzerverwaltung in einem Dictionary simuliert.
# Frage den Benutzer ob er sich anmelden, Registrieren oder das Programm beenden möchte.
# Eine Registrierung wird in einem Dictionary gespiechert mit einem Namen und dem Alter
# Fange folgende Fehler ab: Der Name darf nicht leer sein und das Alter muss eine ganze Zahl sein.
# Wenn der Benutzer sich anmelden möchte, muss er nur seinen Namen eingeben.
# Wenn der Benutzer im Dicitonary vorhanden ist, gib seinen Namen und sein Alter aus.
# Wenn der Benutzer nicht im Dictionary gefunden wird, wird eine Fehlermeldung angezeigt durch einen KeyError.

user_db = {
    "Daniel": 25,
    "Lukas": 30,
    "Serhat": 15,
    "Georg": 66,
    "Mandy": 11,
}

def input_str(question: str) -> str | None:
    input_str = ""
    try:
        input_str = str(input(f"{question}: "))
    except ValueError:
        print("ValueError: Sie haben keine Zeichenkette eingegeben.")
        return None
    else:
        if not input_str:
            print("EmptyStringError: Sie haben eine leere Zeichenkette eingegeben.")
            return None
        return input_str

def input_int(question: str) -> int | None:
    try:
        return int(input(f"{question}: "))
    except ValueError:
        print("ValueError: Sie haben keine ganze Zahl eingegeben.")
        return None

def register_user():
    name = input_str("Bitte geben Sie Ihren Namen ein")
    if not name: return
    
    age = input_int("Bitte geben Sie Ihr Alter ein")
    if not age: return
    
    if name in user_db:
        print(f"Benutzer {name} existiert bereits.")
        return
    
    user_db[name] = age
    print(f"Benutzer {name} wurde erfolgreich registriert")
    
def login_user():
    name = input_str("Bitte geben Sie Ihren Namen ein")
    if not name: return
    
    try:
        age = user_db[name]
        print(f"Benutzer {name} ist {age} Jahre alt")
    except KeyError:
        print("Fehler: Benutzer nicht gefunden!")
        return
        
while True:
    print("\nBenutzerverwaltung: Hauptmenü")
    print("1. Anmelden")
    print("2. Registrieren")
    print("3. Beenden")
    
    choice = input_int("Bitte wählen Sie eine Option")
    print()
    if choice == 1:
        login_user()
    elif choice == 2:
        register_user()
    elif choice == 3:
        print("Programm wird beendet..")
        exit(0)
    else:
        print("Fehler: Ungültige Option. Versuchen Sie es erneut..")