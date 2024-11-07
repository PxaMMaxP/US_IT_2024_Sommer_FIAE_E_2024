# Aufgabe 7
# Erstelle ein Dictionary mit fünf Tieren und deren Anzahl im Lager aus einem Tierhandel. Schreibe ein
# Programm, das die Summe aller Werte im Dicitonary berechnet und ausgibt.

animals = {
    "Hund": 10,
    "Katze": 5,
    "Maus": 20,
    "Kaninchen": 15,
    "Hamster": 30
}

sum = 0
for amount in animals.values():
    sum += amount
    
print(f"Die Summe aller Tiere beträgt {sum}")