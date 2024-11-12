# Aufgabe 10
# Erstelle ein Wörterbuch, welches die Preise von 5 Artikeln speichert. Verwende items() um durch die Schlüssel Wert Paare zu iterieren
# und alle Artikel, deren Preis über 10 € liegt, auszugeben

articles = {
    "Pferdefuß": 5,
    "Pferdefuß-5-er-Pack": 25,
    "Pferdefuß-10-er-Pack": 50,
    "Pferdefuß-20-er-Pack": 100,
    "Pferdefuß-50-er-Pack": 250,   
}

for article, price in articles.items():
    if price > 10:
        print(article)