**Frage 1**: Betrachten Sie den folgenden Python-Code und sagen Sie die Ausgabe voraus:
```python
x = [i * 2 for i in range(6) if i % 2 == 0]
print(x)
```
- `[2, 4, 6, 8, 10]`
- `[0, 4, 8]`
- `[0, 2, 4, 6, 8, 10]`
- `[0, 4, 8, 12]`

**Antwort**: `[0, 4, 8]`

---

**Frage 2**: Ordnen Sie die Phasen des agilen Softwareentwicklungsprozesses in die korrekte Reihenfolge:
- Sprint Planung
- Sprint Durchführung
- Release
- Review
- Retrospektive

Möglichkeiten:
- `Sprint Planung → Sprint Durchführung → Review → Retrospektive → Release`
- `Sprint Durchführung → Sprint Planung → Retrospektive → Review → Release`
- `Review → Sprint Durchführung → Retrospektive → Sprint Planung → Release`

**Antwort**: `Sprint Planung → Sprint Durchführung → Review → Retrospektive → Release`

---

**Frage 3**: Welche der folgenden Bedingungen sind in Python immer wahr?
- `len([1, 2, 3]) < 2`
- `5 > 3 and 3 > 1`
- `"a" > "z"`
- `"hello" in "hello world"`

**Antwort**: `5 > 3 and 3 > 1` & `"hello" in "hello world"`

---

**Frage 4**: Was gibt folgende Funktion zurück?
```python
def multiply(a, b=5):
    return a * b

result = multiply(3)
print(result)
```
- `15`
- `5`
- `3`
- `Es tritt ein Fehler auf.`

**Antwort**: `15`

---

**Frage 5**: Angenommen, Sie haben zwei Listen in Python:
```python
a = [1, 2, 3]
b = a
```
Wie lautet das Ergebnis von `a is b` und `a == b`?
- `a is b ist falsch, a == b ist wahr.`
- `a is b ist wahr, a == b ist falsch.`
- `a is b ist wahr, a == b ist wahr.`
- `Beide sind falsch.`

**Antwort**: `a is b ist wahr, a == b ist wahr.`

---

**Frage 6**: Welche Aussage führt zu einem KeyError in einem Dictionary `person = {"name": "Alex", "age": 30}`?
- `person["name"]`
- `person.get("address")`
- `person["age"]`
- `person["address"]`

**Antwort**: `person["address"]`

---

**Frage 7**: Der folgende Code enthält einen Fehler. Welcher Typ von Fehler ist es?
```python
my_list = [1, 2, 3]
print(my_list[5])
```
Mögliche Antworten:
- `ValueError`
- `IndexError`
- `TypeError`
- `KeyError`

**Antwort**: `IndexError`

---

**Frage 8**: Betrachten Sie den folgenden Code und sagen Sie die Ausgabe voraus:
```python
text = "Python"
print(text[1:4])
```
- `Pyt`
- `yth`
- `ytho`
- `Pyth`

**Antwort**: `yth`

---

**Frage 9**: Betrachten Sie den folgenden Code und sagen Sie die Ausgabe voraus:
```python
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)
```
- `(1, 2, 3)`
- `[1, 2, 3]`
- `{1, 2, 3}`
- `(1, 2, 3, 4)`

**Antwort**: `(1, 2, 3)`

---

**Frage 10**: Welcher Code führt in einem Dictionary zu einem Fehler?
```python
data = {"key1": 100, "key2": 200}
```
Möglichkeiten:
- `data.get("key1")`
- `"key1" in data`
- `data.keys()`
- `data["key3"]`

**Antwort**: `data["key3"]`

---

**Frage 11**: Betrachten Sie den folgenden Code. Welche Ausgabe wird erzeugt?
```python
for i in range(3):
    if i % 2 == 0:
        print("even", i)
    else:
        print("odd", i)
```
- `odd 1, even 2, odd 3`
- `even 0, even 1, even 2`
- `even 0, odd 1, even 2`
- `odd 0, even 1, odd 2`

**Antwort**: `even 0, odd 1, even 2`

---

**Frage 12**: Was gibt die folgende Funktion zurück?
```python
def square(num):
    return num * num

result = square(4)
print(result)
```
- `8`
- `4`
- `16`
- `Fehler`

**Antwort**: `16`

---

**Frage 13**: Welche der folgenden Bedingungen führt in Python zu einem Syntaxfehler?
```python
a, b = 1, 2
```
Möglichkeiten:
- `a == b`
- `a = b`
- `a === b`
- `a != b`

**Antwort**: `a = b` & `a === b`

---

**Frage 14**: Ordnen Sie die folgenden Schritte in einem Projekt der richtigen Reihenfolge zu:
- Testen
- Planung
- Entwicklung
- Deployment

Möglichkeiten:
- `Planung → Entwicklung → Testen → Deployment`
- `Planung → Testen → Entwicklung → Deployment`
- `Testen → Planung → Entwicklung → Deployment`
- `Planung → Deployment → Entwicklung → Testen`

**Antwort**: `Planung → Entwicklung → Testen → Deployment`

---

**Frage 15**: Welche Aussagen werden als wahr ausgewertet?
- `"Python".startswith("Py")`
- `len("Python") > 10`
- `"Python".endswith("n")`
- `10 == "10"`

**Antwort**: `"Python".startswith("Py")` & `"Python".endswith("n")`
