# Aufgabe 5
# Wenn der Benutzer einen Namen eingibt, der nicht im Dictionary existiert, soll eine Meldung
# "Fehler: Name nicht gefunden!" ausgegeben werden. Verwende KeyError.
 
mitarbeiter = {
    "Daniel": 25,
    "Lukas": 30,
    "Serhat": 15,
    "Georg": 66,
    "Mandy": 11,
}

def input_str(question: str) -> str:
    try:
        return str(input(f"{question}: "))
    except ValueError:
        print("ValueError: Sie haben keine Zeichenkette eingegeben. Programm wird beendet..")
        exit(-1)
        
try:
    name = input_str("Bitte geben Sie einen Namen ein")
    print(f"Der Mitarbeiter {name} ist {mitarbeiter[name]} Jahre alt")
except KeyError:
    print("Fehler: Name nicht gefunden! Programm wird beendet..")
    exit(-1)