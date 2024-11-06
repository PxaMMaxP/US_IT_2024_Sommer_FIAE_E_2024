# Aufgabe 3
# Erstelle ein Dictionary, das 5 Lebensmittel und ihre Preise enthält. Baue eine Funktion, die neue Produkte und
# deren Preise speichert. Erweitere deine Funktion, indem du nach einem
# Artikel suchst und gib ihn mit seinem Preis aus. Wenn der Artikel nicht gefunden wurde, soll der Artikel gespeichert werden und einen
# Standardpreis von 0 zurückgegeben

groceries = {
    "Apfel": 1.50,
    "Banane": 1.20,
    "Birne": 1.80,
    "Kiwi": 2.00,
    "Orange": 1.00
}

def create_new_entry(dict, name, price = 0.00):
    dict[name] = price
    print(f"{name} wurde hinzugefügt")
    
def check_price(dict, name):
    price = dict.get(name)
    if price is None:
        create_new_entry(dict, name)
    else:
        print(f"{name} kostet {price} Euro")
        
while True:
    try:
        article = input("Lebensmittel oder 'exit' zum Verlassen eingeben: ")
    except KeyboardInterrupt:
        print("\nNein, nein, nein. Du kannst nicht einfach abbrechen. Bitte 'exit' eingeben.")
        continue
    except:
        print("\nFehlerhafte Eingabe.\nVersuche es erneut.")
        continue
    
    if article == "exit":
        print("Programm beendet.")
        break
    
    check_price(groceries, article)