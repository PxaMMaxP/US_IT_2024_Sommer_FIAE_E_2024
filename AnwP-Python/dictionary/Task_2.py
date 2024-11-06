# Aufgabe 2
# Erstelle ein Dictionary mit den Namen von 5 Mitarbeitern und ihren Positionen in einem Betrieb.
# Schreibe ein Programm, das einen Benutzer nach dem Namen fragt und entweder die Position des
# Mitarbeiters ausgibt oder "Mitarbeiter konnte nicht gefunden werden" anzeigt, wenn der Name
# nicht im Dicitonary vorhanden ist (benutze get() )

mitarbeiter = {
    "Max": "CEO",
    "Hans": "CTO",
    "Lisa": "CFO",
    "Anna": "HR",
    "Peter": "Marketing"
}

def get_position(name):
    position = mitarbeiter.get(name)
    if position is None:
        print("Mitarbeiter konnte nicht gefunden werden")
    else:
        print(f"{name} ist {position}")
        
while True:
    try:
        name = input("Name oder 'exit' zum Verlassen eingeben: ")
    except KeyboardInterrupt:
        print("\nNein, nein, nein. Du kannst nicht einfach abbrechen. Bitte 'exit' eingeben.")
        continue
    except:
        print("\nFehlerhafte Eingabe.\nVersuche es erneut.")
        continue
    
    if name == "exit":
        print("Programm beendet.")
        break
    
    get_position(name)