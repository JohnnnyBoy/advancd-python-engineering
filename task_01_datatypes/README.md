# Task 01: Werte, Datentypen und Kollektionen

In diesem ersten Aufgabenblock liegt der Fokus auf dem Fundament von Python. Ziel ist es, ein tiefes Verständnis für die interne Logik von Datentypen, deren Konvertierung und das Handling komplexer Kollektionen (Listen, Tupel, Dictionaries) zu entwickeln.

## 📋 Aufgabenstellung

### 1. Grundlagen & Typisierung (Aufgabe 2)
* Erstellung der Datei `lab_01_values_types.py`.
* Initialisierung von Variablen für alle Kern-Datentypen:
  * **Zahlen:** `int`, `float`, `complex`
  * **Sequenzen:** `str`, `bytes`, `tuple`, `list`, `bytearray`
  * **Mengen:** `set`, `frozenset`
  * **Mappings:** `dict`
  * **Speziell:** `bool`, `NoneType`
* Überprüfung der Typen mittels `type()` und Experimente mit `print()`-Ausgaben.

### 2. Logik der Typumwandlung (Aufgabe 3 & 4)
* **Type Casting:** Explizite Umwandlung zwischen `int`, `float`, `str` und `bool`.
* **Fehleranalyse:** Untersuchung von Grenzfällen (z. B. String-zu-Int Konvertierung bei nicht-numerischen Inhalten).
* **CLI-Interaktion:** Nutzung des Python-Interpreters in der Kommandozeile (`REPL`), um Cast-Funktionen wie `complex()`, `dict()`, `list()` etc. schnell zu testen.

### 3. Arbeiten mit Sequenzen (Aufgabe 5)
* Vergleich von `str`, `tuple` und `list`.
* **Indizierung & Slicing:** Gezielter Zugriff auf Teilbereiche von Daten.
* **Mitgliedschaft:** Einsatz der Keywords `in` und `not in`.
* **Dynamik:** Nutzung von Listen-Methoden wie `.append()` und `.extend()`.

### 4. Dictionary Deep-Dive (Aufgabe 6)
* Erstellung und Manipulation von Key-Value-Paaren.
* **Workflow:** 
  1. Initialisierung mit `None`.
  2. Nachträgliche Zuweisung von Werten ("Hans", 21, "m").
  3. Verschachtelung: Speichern von Dictionaries innerhalb einer Liste (`mylist`).
* **Referenz-Check:** Beobachtung, wie sich Änderungen in den Dictionaries auf die übergeordnete Liste auswirken.
* **Erweiterung:** Dynamisches Hinzufügen neuer Keys (z. B. "Stadt").

---

## 🛠️ Implementierung & Beobachtungen

> [!TIP]
> **Erkenntnis zur Typumwandlung:** Bei der Konvertierung zu `bool` werden in Python alle "leeren" Objekte (0, "", [], None) als `False` gewertet, alles andere als `True`.

### Verwendete Dateien:
* `lab_01_values_types.py`: Hauptskript mit den Experimenten zu Datentypen.
* `test_datatypes.py`: (Optional) Eigene Test-Logik zur Verifizierung der Dictionary-Struktur.

---
## 🏁 Ergebniskontrolle
Die finale Liste `mylist` weist folgende Struktur auf:
```python
[
    {'Name': 'Hans', 'Alter': 21, 'Geschlecht': 'm', 'Stadt': 'Ingolstadt'},
    {'Name': 'Stefani', 'Alter': 20, 'Geschlecht': 'w', 'Stadt': 'Eichstädt'}
]
