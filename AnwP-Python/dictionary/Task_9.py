# Aufgabe 9
# Erstelle ein Dictionary, das den Umsatz verschiedener Filialen eines Unternehmens speichert.
# Nutze den Filialnamen als Schlüssel und den Umsatz als Wert.
# Schreibe ein Programm, das die Filiale mit dem höchsten Umsatz identifiziert und den Namen
# der Filiale sowie den Umsatz ausgibt

branches_turnover = {
    "Pferdehandel Dreifuß": 100000,
    "Pferdehandel Hamburg": 200000,
    "Pferdehandel München": 300000,
    "Pferdehandel Köln": 400000,
    "Pferdefußhandel Berlin": 500000,
}

max_turnover = max(branches_turnover.values())

for branch, turnover in branches_turnover.items():
    if turnover == max_turnover:
        print(f"Die Filiale mit dem höchsten Umsatz ist {branch} mit einem Umsatz von {turnover} Euro")
        break