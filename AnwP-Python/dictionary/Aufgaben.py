# Aufgabe 1
# Erstelle ein Dictionary, das die Noten eines Schülers in verschiedenen Fächern speichert.
# Schreibe ein Programm, das die Note für ein Fach abfragt und ausgibt. Verwende get() und
# fange mit if und else einen Fehler ab, falls das Fach nicht existiert.
 
 
# AUfgabe 2
# Erstelle ein Dictionary mit den Namen von 5 Mitarbeitern und ihren Positionen in einem Betrieb.
# Schreibe ein Programm, das einen Benutzer nach dem Namen fragt und entweder die Position des
# Mitarbeiters ausgibt oder "Mitarbeiter konnte nicht gefunden werden" anzeigt, wenn der Name
# nicht im Dicitonary vorhanden ist (benutze get() )
 
 
# Aufgabe 3
# Erstelle ein Dictionary, das 5 Lebensmittel und ihre Preise enthält. Baue eine Funktion, die neue Produkte und
# deren Preise speichert. Erweitere deine Funktion, indem du nach einem
# Artikel suchst und gib ihn mit seinem Preis aus. Wenn der Artikel nicht gefunden wurde, soll der Artikel gespeichert werden und einen
# Standardpreis von 0 zurückgegeben
 
 
# Aufgabe 4
# Erstelle ein Dicitonary mit dem Namen und dem Alter von 3 Personen. Schreibe ein Programm, das durch die Schlüssel des
# Dictionaries iteriert und nur die Namen der Personen ausgibt
 
 
# Aufgabe 5
# Gegeben ist ein Dictionary, das die Lagerbestände eines Geschäfts speichert.
# Schreibe ein Programm, das alle Artilkel ausgibt, die aktuell im Lager sind
# (Tipp: Schlüssel mit Wert > 0)
 
 
articles = {
    "Screws": 10000,
    "Wood": 0,
    "Nails": 100,
    "toolkit": 10,
    "scanner": 2,
    "paper": 0,
}
 
 
# Aufgabe 6
# Du findest ein Dictionary mit Ländern als Schlüssel und deren Bevölkerungszahlen als Wert.
# Schreibe ein Programm, das die Länder nach Namen sortiert und in alphabetischer Reihenfolge
# die Namen ausgibt
 
countries = {
    "Deutschland": 85000000,
    "Frankreich": 68000000,
    "Spanien": 47000000,
    "Polen": 36000000,
}
 
 
# Aufgabe 7
# Erstelle ein Dictionary mit fünf Tieren und deren Anzahl im Lager aus einem Tierhandel. Schreibe ein
# Programm, das die Summe aller Werte im Dicitonary berechnet und ausgibt.
 
 
# Aufgabe 8
# Du findest ein Dictionary mit den Namen von Schülern als Schlüssel und deren Noten als Werte.
# Schreibe ein Programm, das den Notendurchschnitt aller Noten berechnet (benutze values() und keys())
 
students = {
    "Alan": 1,
    "Jacques": 6,
    "Gerhard": 1,
    "Willi": 4,
    "Susanne":2
}
 
 
# Aufgabe 9
# Erstelle ein Dictionary, das den Umsatz verschiedener Filialen eines Unternehmens speichert.
# Nutze den Filialnamen als Schlüssel und den Umsatz als Wert.
# Schreibe ein Programm, das die Filiale mit dem höchsten Umsatz identifiziert und den Namen
# der Filiale sowie den Umsatz ausgibt
 
 
 
# Aufgabe 10
# Erstelle ein Wörterbuch, welches die Preise von 5 Artikeln speichert. Verwende items() um durch die Schlüssel Wert Paare zu iterieren
# und alle Artikel, deren Preis über 10 € liegt, auszugeben
 
 
# Aufgabe 11
# Erstelle ein Dictionary, das die Punktzahl von Spielern in einem Videospiel speichert.
# Der Spielername ist der Schlüssel und die Punktzahl der Wert. Schreibe ein Programmm, welches den Spieler ausgibt,
# der die höchste Punktzahl hat. (Benutze items())
 
 
# AUfgabe 12
# Erstelle ein Dictionary mit Informationen über einen Film (z.B.: Titel, Jahr, Genre). Schreibe ein Programm dass das Dictionary
# mithilfe von update um die Bewertung des Films erweitert.
 
 
# Aufgabe 13
# Erstelle 2 Dictionaries die jeweils den Lagerbestand in zwei verschiedenen Filialen eines Geschäfts darstellen.
# Schreibe ein Programm das den Lagerbestand der beiden Filialen zusammenführt (benutze Update) und gib das
# kombinierte Dicitonary aus
 
 
# Aufgabe 14
# Du findest ein Dictionary mit Produkten und ihren Preisen Schreibe ein Programm, das den Benutzer auffordert, den Preis eines Produkts zu
# aktualisieren. Verwende update() um das Produkt mit dem neuen Preis im Dicitonary zu aktualisieren.
 
 
# Aufgabe 15
# Erstelle ein Dictionary mit dem Namen von drei Klassenkameraden und deren Handynummern. Schreibe ein Programm,
# dass das Dicitonary mit clear() leert und überprüft, ob es nun leer ist.
 
 
# Aufgabe 16
# Du findest ein Dictionary mit 5 Studenten und deren Noten.
# Aufgabe 16.1
# Erstelle eine Funktion, die einen neuen Studenten und seine Note nach der Eingabe eines Benutzers in dem Dictionary speichert, allerdings nur, wenn weniger als
# 5 Studenten in dem Dictionary gespeichert sind.
# Aufgabe 16.2
# Falls schon 5 Studenten in dem Dicitonary gespeichert sind, weise darauf hin, dass schon 5 Studenten gespeichert sind und
# stelle den Benutzer vor eine Wahl, ob er das aktuelle Dictionary löschen möchte um den neuen Studenten dort abspeichern zu können, gib währenddessen den
# Notendurchschnitt aller Studenten aus.
# Aufgabe 16.3
# Wenn der Benutzer sich gegen das Löschen der Daten entscheidet, beende das Programm.
# Aufgabe 16.4
# Wenn der Benutzer die Daten löschen will, rufe eine neue Funktion die du jetzt neu bauen wirst auf,
# welche als Parameter die Daten des neuen Studenten als Dictionary empfängt,
# Aufgabe 16.5
# lösche in deiner neuen Funktion, die du sinnvoll benannt hast alle Daten in dem Dicitonary student_graduations
# Aufgabe 16.6
# Stelle den Benutzer noch einmal in deiner neuen Funktion vor eine Auswahl, ob er die Daten die du Übergeben hast, in dem Dictionary student_graduations speichern will.
# Entscheidet sich der Benutzer die Daten zu speichern, speichere die neuen Daten in dem Dicitonary und gib dein Dictionary aus.
# Entscheidet sich der Nutzer gegen das speichern, sollte ein leeres Objekt angezeigt werden