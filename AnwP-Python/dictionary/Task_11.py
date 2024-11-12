# Aufgabe 11
# Erstelle ein Dictionary, das die Punktzahl von Spielern in einem Videospiel speichert.
# Der Spielername ist der Schlüssel und die Punktzahl der Wert. Schreibe ein Programmm, welches den Spieler ausgibt,
# der die höchste Punktzahl hat. (Benutze items())

player = {
    "Max": 100,
    "Moritz": 200,
    "Maurice": 300,
    "Marvin": 400,
    "Marius": 500,
}

max_score = max(player.values())

for name, score in player.items():
    if score == max_score:
        print(f"Der Spieler mit der höchsten Punktzahl ist {name} mit {score} Punkten")
        break