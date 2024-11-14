# Aufgabe 1
# Schreibe ein Programm, das den Benutzer auffordert, eine ganze Zahl einzugeben und diese Zahl verdoppelt.
# Verwende deine Kenntnisse im Error Handling um eine ValueError exception abzufangen, falls der Benutzer
# etwas anderes als eine Zahl eingibt.

try:
    input_number = int(input("Bitte geben Sie eine ganze Zahl ein: "))
except ValueError:
    print("Sie haben keine ganze Zahl eingegeben. Programm wird beendet..")
    exit(-1)
else:
    print(f"Die eingegebene Zahl verdoppelt: {input_number * 2}")