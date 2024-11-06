# Aufgabe 1
# Erstelle ein Dictionary, das die Noten eines Schülers in verschiedenen Fächern speichert.
# Schreibe ein Programm, das die Note für ein Fach abfragt und ausgibt. Verwende get() und
# fange mit if und else einen Fehler ab, falls das Fach nicht existiert.

noten = {
    "Mathe": 1,
    "Deutsch": 2,
    "Englisch": 3,
    "Sport": 4,
    "Kunst": 5
}
 
def get_grade(subject):
    grade = noten.get(subject)
    if grade is None:
        print("Fach nicht gefunden")
    else:
        print(f"Note in {subject}: {grade}")

while True:
    try:
        subject = input("Fach oder 'exit' zum Verlassen eingeben: ")
    except KeyboardInterrupt:
        print("\nNein, nein, nein. Du kannst nicht einfach abbrechen. Bitte 'exit' eingeben.")
        continue
    except:
        print("\nFehlerhafte Eingabe.\nVersuche es erneut.")
        continue
    
    if subject == "exit":
        print("Programm beendet.")
        break
    
    get_grade(subject)