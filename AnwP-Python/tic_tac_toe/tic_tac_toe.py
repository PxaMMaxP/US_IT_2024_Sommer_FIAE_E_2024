import os # Zusätzlich eingefügt, um das Terminal zu leeren; Ist nicht Teil der Aufgabe!

def berechne_punkte(spielfeld, koordinaten):
    '''Berechnet die Punkte für eine Reihe von Feldern.
    Für jedes Feld, das von Spieler X belegt ist, wird 1 Punkt hinzugefügt.
    Für jedes Feld, das von Spieler O belegt ist, wird 1 Punkt abgezogen.
    Die Gesamtpunktzahl wird zurückgegeben. 
    Daher ist die Gesamtpunktzahl 3, wenn alle Felder von Spieler X belegt sind
    und -3, wenn alle Felder von Spieler O belegt sind.'''
    
    punkte = 0
    for koordinate in koordinaten:
        if spielfeld[koordinate[0]][koordinate[1]] == 'X': 
            punkte += 1
        elif spielfeld[koordinate[0]][koordinate[1]] == 'O': 
            punkte -= 1
    return punkte

def pruefe_gewinner(spielfeld):
    '''Überprüft, ob ein Spieler gewonnen hat.
    Wenn ein Spieler gewonnen hat, wird das Zeichen des Spielers zurückgegeben.
    Sonst wird None zurückgegeben.'''
    
    # Zur Vermeidung von *Magic Numbers* (Zahlen, die ohne Kontext schwer zu verstehen sind)
    # definieren wir die Punkte, die ein Spieler erhalten muss, um zu gewinnen.
    punkte_x_gewonnen = 3
    punkte_o_gewonnen = -3
    
    # Die Koordinaten der Felder, die zu einer Gewinnreihe führen können.
    koordinaten = [
        [(0, 0), (0, 1), (0, 2)], # Horizontale Reihen
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], # Vertikale Reihen
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], # Diagonale Reihen
        [(0, 2), (1, 1), (2, 0)]
    ]
    
    # Jede mögliche Gewinnreihe wird überprüft.
    for koordinate in koordinaten:
        punkte = berechne_punkte(spielfeld, koordinate)
        if punkte == punkte_x_gewonnen:
            return 'X'
        elif punkte == punkte_o_gewonnen:
            return 'O'
    return None

def ist_spielfeld_voll(spielfeld):
    '''Überprüft, ob das Spielfeld voll ist.
    Wenn auch nur ein einziges Feld leer ist, wird False zurückgegeben
    um anzuzeigen, dass das Spielfeld nicht voll ist.
    Sonst wird True zurückgegeben um anzuzeigen, dass das Spielfeld voll ist.'''
    
    for zeile in spielfeld:
        for feld in zeile:
            if feld == ' ':
                return False
    return True

def zeichne_spielfeld(spielfeld):
    '''Leert das Terminal und zeichnet das Spielfeld.'''
    
    os.system('cls') # Das habe ich zusätzlich eingefügt, um das Spielfeld zu leeren; Ist nicht Teil der Aufgabe!
    print("\n")
    # Geht alternativ auch mit einer List Comprehension: [print(" | ".join(zeile) + "\n---------") for zeile in Spielfeld]
    for zeile in spielfeld:
        print(" | ".join(zeile))
        print("---------")

def starte_spiel():
    '''Startet das Spiel.'''
    # Zur Vermeidung von *Magic Numbers* (Zahlen, die ohne Kontext schwer zu verstehen sind)
    # definieren wir die Min- und Max-Werte für die Eingabe.
    minInput = 0
    maxInput = 2
    
    spielfeld = [[' ' for j in range(3)] for i in range(3)]
    aktueller_spieler = 'X'
    
    zeichne_spielfeld(spielfeld)
    print("Aktueller Spieler: " + aktueller_spieler)
    
    while True:
        # Abfrage der Zeile und Spalte, die der Spieler belegen möchte
        # und korrektur der Eingabe auf gültige Werte.
        # Die Eingabe wird daher um 1 verringert, da die Indizes bei 0 beginnen.
        try:
            zeile = int(input("Bitte Zeile (1-3) eingeben: ")) - 1
            spalte = int(input("Bitte Spalte (1-3) eingeben: ")) - 1
        except:
            # Abfangen von *allen* Fehlern, die auftreten können, wenn der Benutzer keine Zahl eingibt.
            print("Ungültige Eingabe; Bitte nur Zahlen zwischen 1 und 3 eingeben!\nVersuche es erneut..")
            continue
        
        if zeile < minInput or zeile > maxInput or spalte < minInput or spalte > maxInput:
            print("Ungültige Eingabe; Bitte nur Zahlen zwischen 1 und 3 eingeben!\nVersuche es erneut..")
            continue
        
        if spielfeld[zeile][spalte] != ' ':
            print("Feld ist bereits belegt!\nVersuche es erneut..")
            continue
        
        # Wenn die Eingabe gültig ist und das Feld leer ist, 
        # wird das Feld mit dem aktuellen Spieler belegt.
        spielfeld[zeile][spalte] = aktueller_spieler
        
        # Abhängig vom aktuellen Spieler wird der Spieler gewechselt.
        if aktueller_spieler == 'X':
            aktueller_spieler = 'O'
        else:
            aktueller_spieler = 'X'
        
        zeichne_spielfeld(spielfeld)
        
        gewinner_ist = pruefe_gewinner(spielfeld)
        
        if gewinner_ist == 'X':
            print("Spieler X hat gewonnen!")
            break
        elif gewinner_ist == 'O':
            print("Spieler O hat gewonnen!")
            break
        elif ist_spielfeld_voll(spielfeld):
            print("Das Spiel ist unentschieden geendet!")
            break
        
        print("Aktueller Spieler: " + aktueller_spieler)


starte_spiel()