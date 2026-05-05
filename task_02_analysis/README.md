# 📊 Task 02: Zahlen-Analyse-Tools

In diesem Modul liegt der Fokus auf der Implementierung mathematischer Algorithmen, der Validierung von Benutzereingaben und der sauberen Fehlerbehandlung in Python. Es deckt physikalische Umrechnungen sowie zahlentheoretische Analysen ab.

## 📂 Enthaltene Programme

### 1. 🌡️ Temperatur-Konverter (`temp_converter.py`)
Dieses Tool ermöglicht die präzise Umrechnung zwischen verschiedenen Temperaturskalen.
* **Funktionen:** Umrechnung zwischen Celsius, Kelvin und Fahrenheit.
* **Sicherheit:** 
  * Nutzung von `assert`, um physikalisch unmögliche Werte (unter dem absoluten Nullpunkt) abzufangen.
  * `try-except` Blöcke zur Behandlung von `ValueErrors` bei Falscheingaben.
* **Interaktion:** Endlosschleife mit "Exit"-Funktion für eine benutzerfreundliche Bedienung.

### 2. 🔢 Primzahl-Checker (`prime_checker.py`)
Ein dediziertes Programm zur Identifizierung von Primzahlen basierend auf der klassischen Teilbarkeitsprüfung.
* **Logik:** Prüfung aller Teiler von 2 bis zur Hälfte der Zahl (`n // 2`).
* **Besonderheit:** Im Falle einer Nicht-Primzahl wird der kleinste gefundene Teiler ausgegeben.
* **Validierung:** Strikte Einhaltung der mathematischen Definition (Ganzzahl > 1) via `assert`.

### 3. 🔍 Universal Zahlen-Analyse-Tool (`analysis_tool.py`)
Ein fortgeschrittenes Analyse-Tool, das mehrere mathematische Konzepte in einer modularen Architektur vereint.
* **Analyse-Modi:**
  * **Prime:** Effiziente Prüfung (optimiert bis $\sqrt{n}$).
  * **Armstrong:** Identifikation narzisstischer Zahlen (Summe der Ziffernpotenzen).
  * **Perfect:** Prüfung auf perfekte Zahlen (Summe der echten Teiler).
* **Software-Design:** Konsequenter Verzicht auf globale Variablen; alle Logiken sind in Funktionen mit lokalem Scope gekapselt.

---

## 🛠️ Technische Konzepte & Lernziele

| Konzept | Umsetzung in dieser Aufgabe |
| :--- | :--- |
| **Input Validation** | Einsatz von `assert` zur Sicherstellung der Datenintegrität. |
| **Error Handling** | Abfangen von Konvertierungsfehlern (`ValueError`) und Logikfehlern. |
| **Algorithmen** | Implementierung von Schleifen (`while`, `for`) und Modulo-Operationen `%`. |
| **String Formatting** | Hochwertige UI-Ausgabe mittels f-Strings und Format-Specifiern (z. B. `:8.2f`). |

---

## 🖥️ Anwendungsbeispiele (Output)

#### Beispiel: Armstrong-Zahl Analyse
```text
- Zahlen-Analyse-Tool -
Verfügbare Analysen: [prime] | [armstrong] | [perfect] | [exit]
Wahl treffen: armstrong
Welche Zahl soll auf 'armstrong' geprüft werden? 371
 Ergebnis: Die Zahl 371 ist eine Armstrong-Zahl.
