# Aufgabe 8
# Schreibe ein Programm, das die Variable namens zahl verwendet und diese mit einem Wert von 10 Multipliziert.
# Verwende Error Handling um einen NameError abzufangen, für den Fall, das die Variable nicht definiert wurde.

# zahl = 5

MULTIPLIER = 10 # *Magic Number*: Konstante, die den Wert 10 als Multiplikator speichert

try:
    print(zahl * MULTIPLIER)
except NameError:
    print("NameError: Die Variable 'zahl' ist nicht definiert. Programm wird beendet..")
    exit(-1)