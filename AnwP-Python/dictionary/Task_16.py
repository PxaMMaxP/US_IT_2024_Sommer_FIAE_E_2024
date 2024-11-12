# Aufgabe 16
# Du findest ein Dictionary mit 5 Studenten und deren Noten.
# Aufgabe 16.1
# Erstelle eine Funktion, die einen neuen Studenten und seine Note nach der Eingabe eines Benutzers in dem Dictionary speichert, allerdings nur, wenn weniger als
# 5 Studenten in dem Dictionary gespeichert sind.
# Aufgabe 16.2
# Falls schon 5 Studenten in dem Dicitonary gespeichert sind, weise darauf hin, dass schon 5 Studenten gespeichert sind und
# stelle den Benutzer vor eine Wahl, ob er das aktuelle Dictionary löschen möchte um den neuen Studenten dort abspeichern zu können, gib währenddessen den
# Notendurchschnitt aller Studenten aus.
# Aufgabe 16.3
# Wenn der Benutzer sich gegen das Löschen der Daten entscheidet, beende das Programm.
# Aufgabe 16.4
# Wenn der Benutzer die Daten löschen will, rufe eine neue Funktion die du jetzt neu bauen wirst auf,
# welche als Parameter die Daten des neuen Studenten als Dictionary empfängt,
# Aufgabe 16.5
# lösche in deiner neuen Funktion, die du sinnvoll benannt hast alle Daten in dem Dicitonary student_graduations
# Aufgabe 16.6
# Stelle den Benutzer noch einmal in deiner neuen Funktion vor eine Auswahl, ob er die Daten die du Übergeben hast, in dem Dictionary student_graduations speichern will.
# Entscheidet sich der Benutzer die Daten zu speichern, speichere die neuen Daten in dem Dicitonary und gib dein Dictionary aus.
# Entscheidet sich der Nutzer gegen das speichern, sollte ein leeres Objekt angezeigt werden

student_graduations = {
    "Max": 1,
    "Moritz": 2,
    "Mia": 3,
    "Marie": 4,
    "Maja": 5
}

def ask_permission(question: str) -> bool:
    """
    Fragt den Benutzer nach einer Erlaubnis und gibt True zurück, wenn der Benutzer Ja eingibt, ansonsten False.
    """
    while True:
        choice = input(f"{question} (Ja/Nein): ")
        if choice == "Ja":
            return True
        elif choice == "Nein":
            return False
        else:
            print("Bitte gib Ja oder Nein ein.")
            continue

def ask_for_student_grade() -> dict:
    """
    Fragt den Benutzer nach dem Namen und der Note eines Studenten und gibt ein Dictionary zurück.
    """
    student = input("Gib den Namen des Studenten ein: ")
        
    while True:
        try:
            grade = float(input("Gib die Note des Studenten ein: "))
        except ValueError:
            print("Bitte versuche es erneut und gib eine Zahl ein..")
            continue
        break
    
    return {student: grade}

def replace_student_grades(new_student_student_graduations: dict):
    """
    Löscht alle Daten in dem Dictionary student_graduations und fragt den Benutzer, ob er die neuen Daten speichern möchte.
    Gibt anschließend das Dictionary aus.
    """
    student_graduations.clear()
    choice = ask_permission("Möchtest du die neuen Daten wirklich speichern?")
    if choice:
        student_graduations.update(new_student_student_graduations)
        
    print("Studenten: ", student_graduations)

def add_student_grade():
    """
    Fügt einen neuen Studenten und seine Note in das Dictionary student_graduations ein, wenn weniger als 5 Studenten gespeichert sind.
    Ansonsten wird der Benutzer gefragt, ob er die aktuellen Daten löschen möchte und ob er die neuen Daten speichern möchte.
    """
    
    student_grade = ask_for_student_grade()
    
    if len(student_graduations) < 5:
        
        student_graduations.update(student_grade)
        print("Studenten: ", student_graduations)
    else:
        print("Es sind schon 5 Studenten gespeichert.")
        print("Notendurchschnitt: ", sum(student_graduations.values()) / len(student_graduations))
        
        choice = ask_permission("Möchtest du die aktuellen Daten löschen?")
        if choice:
            replace_student_grades(student_grade)
        else:
            print("Programm wird beendet")
            

add_student_grade()