# Aufgabe 4
# Erstelle ein Dicitonary mit dem Namen und dem Alter von 3 Personen. Schreibe ein Programm, das durch die Schlüssel des
# Dictionaries iteriert und nur die Namen der Personen ausgibt

people = {
    "Max": 25,
    "Hans": 30,
    "Lisa": 27
}

for name in people.keys():
    print(name)