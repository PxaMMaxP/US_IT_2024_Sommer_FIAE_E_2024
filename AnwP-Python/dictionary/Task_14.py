# Aufgabe 14
# Du findest ein Dictionary mit Produkten und ihren Preisen Schreibe ein Programm, das den Benutzer auffordert, 
# den Preis eines Produkts zu
# aktualisieren. Verwende update() um das Produkt mit dem neuen Preis im Dicitonary zu aktualisieren.

products = {
        "Apfel": 1,
        "Birne": 2,
        "Banane": 3
    }
 
print("Produkte: ", products)

product = input("Welches Produkt möchtest du aktualisieren? ")

if product in products:
    price = float(input("Gib den neuen Preis ein: "))
    products.update({product: price})
    print("Produkte: ", products)
else:
    print("Produkt nicht gefunden")