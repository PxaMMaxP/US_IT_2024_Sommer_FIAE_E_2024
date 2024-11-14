# Aufgabe 3
# Schreibe eine Funktion mit dem Namen teilen, die 2 Zahlen als Parameter erhält und das Ergebnis einer
# Division zurück gibt. Verwende try und except um eine Division durch Null zu verhindern und eine
# entsprechende Fehlermeldung auszugeben

def teilen(a: int, b: int) -> int:
    try:
        return a / b
    except ZeroDivisionError:
        print("ZeroDivisionError: Division durch Null ist nicht erlaubt. Programm wird beendet..")
        exit(-1)