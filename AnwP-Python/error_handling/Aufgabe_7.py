# Aufgabe 7
# Schreibe ein Programm, welches eine Datei mit dem Namen Test in deinem Ordner dateien speichert und schreibe eine kleine Geschichte dort hinein.
# Finde heraus, welcher Modus für das schreiben von Dateien genutzt werden kann.
# Was wäre ein alternativer Modus, wenn du etwas an die Datei anhängen willst ohne die Datei bei dem erneuten ausführen zu überschreiben?

def create_write_file(file_name: str, content: str) -> None:
    try:
        with open(file_name, "w") as file:
            file.write(content)
    except FileNotFoundError:
        print("FileNotFoundError: Datei konnte nicht gefunden werden. Programm wird beendet..")
        exit(-1)
        
def append_file(file_name: str, content: str) -> None:
    try:
        with open(file_name, "a") as file:
            file.write(content)
    except FileNotFoundError:
        print("FileNotFoundError: Datei konnte nicht gefunden werden. Programm wird beendet..")
        exit(-1)


story = "Das ist eine kleine Geschichte von Dr. Evil und seinem Kater Mr. Bigglesworth."
create_write_file("dateien/Test.txt", story) # Beachten: Der Pfad ist relativ zum aktuellen Arbeitsverzeichnis!