# Aufgabe 13
# Erstelle 2 Dictionaries die jeweils den Lagerbestand in zwei verschiedenen Filialen eines Geschäfts darstellen.
# Schreibe ein Programm das den Lagerbestand der beiden Filialen zusammenführt (benutze Update) und gib das
# kombinierte Dicitonary aus

stock1 = {
    "Apfel": 10,
    "Birne": 20,
    "Banane": 30
}

stock2 = {
    "Apfel": 5,
    "Birne": 10,
    "Banane": 15
}

stock1.update(stock2)

print(stock1)