**Frage 1**: Betrachten Sie den folgenden Python-Code und sagen Sie die Ausgabe voraus:
```python
numbers = [i**2 for i in range(5) if i % 2 == 0]
print(numbers)
```
- `[0, 4, 16]`
- `[1, 4, 9, 16]`
- `[0, 1, 4, 9]`
- `[0, 4, 16, 25]`


**Antwort**: `[0, 4, 16]`

---

**Frage 2**: Ordnen Sie die Phasen des agilen Softwareentwicklungsprozesses in die korrekte Reihenfolge:
- Anforderungen definieren
- Implementierung
- Testen
- Deployment
- Wartung

Möglichkeiten:
- `Anforderungen definieren → Implementierung → Testen → Deployment → Wartung`
- `Implementierung → Anforderungen definieren → Testen → Wartung → Deployment`
- `Testen → Implementierung → Anforderungen definieren → Deployment → Wartung`
- `Anforderungen definieren → Deployment → Testen → Implementierung → Wartung`


**Antwort**: `Anforderungen definieren → Implementierung → Testen → Deployment → Wartung`

---

**Frage 3**: Welche der folgenden Bedingungen sind in Python immer wahr?
- `"data" in "database"`
- `len([10, 20, 30, 40]) < 3`
- `8 >= 3 and 3 > 8`
- `7 == 7 or 7 < 5`

Möglichkeiten:
- `Nur "data" in "database"`
- `Nur 7 == 7 or 7 < 5`
- `Beide, "data" in "database" und 7 == 7 or 7 < 5`
- `Keine der Bedingungen`


**Antwort**: `Beide, "data" in "database" und 7 == 7 or 7 < 5`

---

**Frage 4**: Was gibt die folgende Funktion zurück?
```python
def add_values(x, y=5):
    return x + y

result = add_values(7)
print(result)
```
- `12`
- `7`
- `5`
- `Fehler tritt auf`


**Antwort**: `12`

---

**Frage 5**: Angenommen, Sie haben zwei Listen in Python:
```python
a = [10, 20, 30]
b = a[:]
```
Wie lautet das Ergebnis von `a is b` und `a == b`?
- `a is b ist wahr, a == b ist wahr.`
- `a is b ist falsch, a == b ist wahr.`
- `a is b ist wahr, a == b ist falsch.`
- `Beide sind falsch.`


**Antwort**: `a is b ist falsch, a == b ist wahr.`

---

**Frage 6**: Welche Aussage führt zu einem KeyError in einem Dictionary `student = {"name": "Tom", "grade": "A"}`?
- `student["name"]`
- `student.get("age")`
- `student["grade"]`
- `student["age"]`


**Antwort**: `student["age"]`

---

**Frage 7**: Was ist das Ergebnis des folgenden Codes?
```python
items = [1, 2, 3, 4]
tuple_items = tuple(items)
print(tuple_items)
```
- `(1, 2, 3, 4)`
- `[1, 2, 3, 4]`
- `{1, 2, 3, 4}`
- `(2, 3, 4)`


**Antwort**: `(1, 2, 3, 4)`

---

**Frage 8**: Welche der folgenden Bedingungen wird als wahr ausgewertet?
```python
data = {"course": "Python", "level": "beginner"}
```
- `"course" in data`
- `data["course"] == "advanced"`
- `"Python" in data`
- `data.get("level") == "expert"`


**Antwort**: `"course" in data`

---

**Frage 9**: Betrachten Sie folgenden Python-Code. Was ist die erwartete Ausgabe?
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numbers[1::2] = [0] * 6  
print(numbers)
```
- `[1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0]`
- `[1, 3, 5, 7, 9, 11]`
- `[0, 0, 0, 0, 0, 0]`
- `[11, 9, 7, 5, 3, 1]`
- `[11, 0, 9, 0, 7, 0, 5, 0, 3, 0, 1]`


**Antwort**: `[1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0]`

**Kommentar**: What the fuck? Wenn ich so etwas in einem Produktiv-Code sehen würde, gäbe es mit absoluter Sicherheit tote!

---

**Frage 10**: Betrachten Sie den folgenden Python-Code. Was ist die erwartete Ausgabe?
```python
def zeichne_zeichen(muster_liste):
    for anzahl in muster_liste:
        print(anzahl * "x", end=" ")

muster_liste = [2, 4, 1, 3]
zeichne_zeichen(muster_liste)
```
- `xx xxxx x xxx`
- `x xx xxx xxxx`
- `xxxx xx xxx x`
- `x x x x`


**Antwort**: `xx xxxx x xxx`

---

**Frage 11**: Für Ihr Projekt benötigen Sie ein Datenformat, das die Namen von Städten und deren Postleitzahlen speichert. Wählen Sie die richtige Definition des Dictionaries aus.
- `postleitzahlen = {"Berlin": 10115, "Hamburg": 20095}`
- `postleitzahlen = {"Berlin": "10115", "Hamburg": "20095"}`
- `postleitzahlen = {Berlin: "10115", Hamburg: "20095"}`


**Antwort**: `postleitzahlen = {"Berlin": "10115", "Hamburg": "20095"}`

---

**Frage 12**: Betrachten Sie folgenden Code:
```python
zahl = 5
while zahl > 0:
    zahl -= 1
print(zahl)
```
Was ist die erwartete Ausgabe?
- `5`
- `0`
- `1`
- `die Variable ist nicht verfügbar`


**Antwort**: `0`

---

**Frage 13**: Betrachten Sie folgenden Code:
```python
b = 3
if b > 3:
    b += 2
else:
    b -= 2
print(b)
```
Was ist die erwartete Ausgabe?
- `5`
- `1`
- `3`
- `0`


**Antwort**: `1`

---

**Frage 14**: Angenommen, der folgende Code wird fehlerfrei ausgeführt:
```python
x = [10, 20, 30]
y = [10, 15, 30]
```
Welche der folgenden Vergleiche sind False?
- `x[1] > y[1]`
- `x[2] == y[2]`
- `x[0] != y[0]`
- `len(x) == len(y)`


**Antwort**: `x[0] != y[0]`