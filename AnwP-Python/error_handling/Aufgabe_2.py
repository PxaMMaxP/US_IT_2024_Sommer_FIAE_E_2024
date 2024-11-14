# Aufgabe 2
# Schreibe eine Funktion mit dem Namen addieren(a, b), die zwei Zahlen als Parameter empfängt.
# Verwende deine Error Handling Skills um einen TypeError abzufangen, falls einer der Parameter
# kein Zahlentyp ist

def addieren(a: int, b: int) -> int:
    try:
        return a + b
    except TypeError:
        print("TypeError: Einer der Parameter ist kein Zahlentyp. Programm wird beendet..")
        exit(-1)