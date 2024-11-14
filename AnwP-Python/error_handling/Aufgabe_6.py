# Aufgabe 6
# Schreibe ein Programm, dass eine Datei mit dem Namen rechnung.txt öffnet und deren Inhalt auf dem Bildschirm ausgibt
# Erstelle einen Ordner mit dem Namen dateien. Speichere darin eine Datei namens rechnung.txt und finde heraus wie du die Datei öffnen und in der Print ausgabe lesen kannst.
# Verwende FileNotFoundError wenn die Datei nicht existiert.  

def read_print_file(file_name: str) -> None:
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("FileNotFoundError: Datei konnte nicht gefunden werden. Programm wird beendet..")
        exit(-1)
        
read_print_file("./dateien/rechnung.txt") # Beachten: Der Pfad ist relativ zum aktuellen Arbeitsverzeichnis!