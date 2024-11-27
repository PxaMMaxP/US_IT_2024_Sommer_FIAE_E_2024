**Frage 1**: Gegeben ist der folgende Python-Code:
```python
nummern = {"eins": 1, "zwei": 2, "drei": 3}
```
 
Mit welcher Bedingung lässt sich explizit prüfen, ob der Schlüssel "vier" in dem Dictionary nummern vorhanden ist?
- `"vier" in nummern`
- `nummern.get("vier") is not None`
- `nummern.has_key("vier")`
- `"vier" in nummern.keys()`


**Antwort**: 

---

**Frage 2**: Betrachten Sie folgenden Python-Code:
```python
zahlen = [5, 10, 15, 20]
result = [zahl + 2 for zahl in zahlen if zahl > 10]
print(result)
```
 
Was ist die erwartete Ausgabe?
- `[12, 17, 22]`
- `[10, 15, 20, 25]`
- `[17, 22]`
- `[7, 12, 17, 22]`

**Antwort**: 

---

**Frage 3**: Betrachten Sie folgenden Code:
```python
text = "Hallo, Welt!"
if "Welt" in text:
    print("Begrüßung erkannt!")
else:
    print("Keine Begrüßung erkannt.")
```

Was wird ausgegeben?
- `Begrüßung erkannt!`
- `Keine Begrüßung erkannt.`
- `Ein Fehler tritt auf`
- `Es gibt keine Ausgabe`

**Antwort**: 

---

**Frage 4**: Betrachten Sie den folgenden Python-Code:
```python
farben = ["rot", "grün", "blau"]
for index, farbe in enumerate(farben):
    print(index, farbe)
```
 
Was ist die erwartete Ausgabe?
- `1 rot, 2 grün, 3 blau`
- `0 rot, 1 grün, 2 blau`
- `rot, grün, blau`
- `1 rot, 2 grün, 3 blau, Ende der Liste`

**Antwort**: 

---
 
**Frage 5**: Betrachten Sie den folgenden Python-Code:
```python
werte = [10, 20, 30, 40, 50]
ergebnis = werte[1::2]
print(ergebnis)
```
 
Was ist die erwartete Ausgabe?
- `[10, 20, 30, 40, 50]`
- `[20, 40]`
- `[10, 30, 50]`
- `[40, 50]`

**Antwort**: 

---
 
**Frage 6**: Gegeben ist das folgende Dictionary:
```python
produkte = {"Apfel": 1.5, "Banane": 0.8, "Orange": 1.2}
```

Welche der folgenden Optionen gibt True zurück, wenn der Schlüssel "Banane" im Dictionary vorhanden ist?
- `"Banane" in produkte`
- `produkte.has_key("Banane")`
- `produkte.get("Banane") is not None`
- `"Apfel" in produkte.keys()`

**Antwort**: 

---
 
**Frage 7**: Betrachten Sie folgenden Code:
```python
liste = [3, 6, 9, 12, 15, 18]
neue_liste = liste[::2]
print(neue_liste)
```
 
Was ist die erwartete Ausgabe?
- `[6, 12, 18]`
- `[3, 9, 15]`
- `[3, 6, 9, 12, 15, 18]`
- `[6, 9, 12]`

**Antwort**: 

---
 
**Frage 8**: Betrachten Sie den folgenden Python-Code:
```python
def quadrieren(x):
    return x ** 2
 
zahlen = [2, 4, 6]
resultat = [quadrieren(z) for z in zahlen]
print(resultat)
```
 
Was ist die erwartete Ausgabe?
- `[2, 4, 6]`
- `[4, 16, 36]`
- `[8, 64, 216]`
- `[2, 16, 216]`

**Antwort**: 

---
 
**Frage 9**: Gegeben ist das folgende Dictionary:
```python
buch = {"Autor": "Max", "Titel": "Python lernen", "Seiten": 250}
```

Welche der folgenden Ausdrücke geben True zurück, wenn das Schlüssel-Wert-Paar "Titel": "Python lernen" existiert?
- `"Titel" in buch and buch["Titel"] == "Python lernen"`
- `buch.get("Titel") == "Python lernen"`
- `"Python lernen" in buch.values()`
- `"Autor" in buch and buch["Autor"] == "Python lernen"`

**Antwort**: 

---
 
**Frage 10**: Betrachten Sie den folgenden Python-Code:
```python
x = [1, 2, 3]
y = x
x[0] = 10
print(y)
```
 
Was ist die erwartete Ausgabe?
- `[10, 2, 3]`
- `[1, 2, 3]`
- `[1, 10, 3]`
- `Ein Fehler tritt auf`

**Antwort**: 

---

**Frage 11**: Gegeben ist die Liste `zahlen = [5, 10, 15, 20]`. Welche der folgenden Ausdrücke gibt True zurück, wenn die Zahl 15 in der Liste `zahlen` enthalten ist?
- `15 in zahlen`
- `zahlen.count(15) > 0`
- `zahlen.index(15) >= 0`
- `zahlen.find(15)`

**Antwort**: 

---

**Frage 12**: Betrachten Sie den folgenden Python-Code:
```python
text = "Python Programmierung"
print(text[7:11])
```

Was ist die erwartete Ausgabe?
- `rogr`
- `Pyth`
- `Prog`
- `ramm`

**Antwort**: 

---

**Frage 13**: Gegeben ist das folgende Dictionary:
```python
autos = {"BMW": "Deutschland", "Toyota": "Japan", "Ford": "USA"}
```

Welche der folgenden Bedingungen gibt False zurück?
- `"Audi" in autos`
- `autos.get("Toyota") == "Japan"`
- `"Deutschland" in autos.values()`
- `"BMW" in autos`

**Antwort**: 

---

**Frage 14**: Betrachten Sie folgenden Code:
```python
x = [2, 4, 6, 8]
y = x[:]
x[1] = 10
print(y)
```

Was ist die erwartete Ausgabe?
- `[2, 10, 6, 8]`
- `[2, 4, 6, 8]`
- `[10, 4, 6, 8]`
- `[2, 4, 10, 8]`

**Antwort**: 

---

**Frage 15**: Betrachten Sie den folgenden Python-Code:
```python
werte = [10, 20, 30, 40]
ergebnis = [x**2 if x > 20 else x + 5 for x in werte]
print(ergebnis)
```

Was ist die erwartete Ausgabe?
- `[15, 25, 900, 1600]`
- `[15, 25, 35, 45]`
- `[10, 20, 900, 1600]`
- `[5, 10, 15, 20]`

**Antwort**: 

---

**Frage 16**: Betrachten Sie den folgenden Python-Code:
```python
items = {"A": 10, "B": 20, "C": 30}
ergebnis = sum(value for key, value in items.items() if key != "B")
print(ergebnis)
```

Was ist die erwartete Ausgabe?
- `10`
- `20`
- `40`
- `60`

**Antwort**: 

---

**Frage 17**: Gegeben ist die folgende Funktion:
```python
def berechne(wert):
    if wert % 2 == 0:
        return wert ** 2
    else:
        return wert ** 3
```

Was ist die Ausgabe von `berechne(3) + berechne(4)`?
- `12`
- `64`
- `91`
- `43`

**Antwort**: 

---

**Frage 18**: Gegeben ist das folgende Dictionary:
```python
daten = {"Anna": 30, "Ben": 25, "Clara": 35}
```

Welche der folgenden Bedingungen gibt True zurück, wenn alle Alterswerte größer als 20 sind?
- `all(wert > 20 for wert in daten.values())`
- `any(wert > 20 for wert in daten.values())`
- `all(wert < 20 for wert in daten.keys())`
- `any(wert < 20 for wert in daten.keys())`

**Antwort**: 

---

**Frage 19**: Betrachten Sie den folgenden Python-Code:
```python
x = [i for i in range(5)]
y = x
z = x[:]
x[0] = 10
print(y[0], z[0])
```

Was ist die erwartete Ausgabe?
- `0 0`
- `10 10`
- `10 0`
- `Ein Fehler tritt auf`

**Antwort**: 

---

**Frage 20**: Betrachten Sie den folgenden Python-Code:
```python
zahlen = [4, 5, 6, 7]
resultat = [str(x) for x in zahlen if x % 2 == 0]
print(" und ".join(resultat))
```

Was ist die erwartete Ausgabe?
- `"4 und 6"`
- `"4 6"`
- `"5 und 7"`
- `"4 und 5 und 6 und 7"`

**Antwort**: 

---

**Frage 21**: Gegeben ist die folgende Funktion:
```python
def test_funktion(a, b=5):
    return a * b

x = test_funktion(3)
y = test_funktion(3, 4)
print(x, y)
```

Was ist die erwartete Ausgabe?
- `15 12`
- `3 5`
- `15 20`
- `12 15`

**Antwort**: 

---

**Frage 22**: Betrachten Sie folgenden Python-Code:
```python
daten = [1, 2, 3, 4, 5]
daten[1:4] = [10, 20]
print(daten)
```

Was ist die erwartete Ausgabe?
- `[1, 2, 3, 4, 5]`
- `[1, 10, 20, 5]`
- `[1, 10, 20, 4, 5]`
- `[10, 20, 1, 4, 5]`

**Antwort**: 