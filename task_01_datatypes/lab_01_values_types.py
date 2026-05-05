# ==========================================
# Aufgabe 2: Werte und Datentypen
# ==========================================

# Zahlen: int, float, complex
widerstand = 470        # Ganzzahl (int)
spannung = 230.0        # Gleitkommazahl (float)
impedanz = 10 + 5j      # Komplexe Zahl (complex) - Wichtig für Wechselstromtechnik!

print(f"Widerstand: {widerstand}, Typ: {type(widerstand)}")
print(f"Spannung: {spannung}, Typ: {type(spannung)}")
print(f"Impedanz: {impedanz}, Typ: {type(impedanz)}")

# Sequenzen: str, tuple, list, bytes, bytearray
einheit = "Volt"                    # String (str)
punkt = (10, 20)                    # Tuple (unveränderlich)
messwerte = [220.1, 220.5, 219.8]   # List (veränderlich)
rohdaten = b"Start"                 # ByteString (unveränderlich)
puffer = bytearray(5)               # ByteArray (veränderlich)

print(f"\nEinheit: {type(einheit)}, Liste: {type(messwerte)}")
print(f"Rohdaten: {rohdaten}, Typ: {type(rohdaten)}")

# Mengen: set, frozenset
sensoren = {"S1", "S2", "S1"}       # Set - entfernt Duplikate automatisch
konstante_menge = frozenset([1, 2, 3])

print(f"\nSet: {sensoren}, Typ: {type(sensoren)}")
print(f"Frozenset: {konstante_menge}, Typ: {type(konstante_menge)}")

# Abbildungen: Dictionary
messpunkt = {"zeit": 1.5, "wert": 5.2, "einheit": "A"}
print(f"\nDict-Wert Zeit: {messpunkt['zeit']}, Typ: {type(messpunkt)}")

# Bool / NoneType
ist_aktiv = True
fehler_code = None
print(f"Aktiv: {type(ist_aktiv)}, Fehler: {type(fehler_code)}")


# ==========================================
# Aufgabe 3 & 4: Typumwandlungen (Casting)
# ==========================================

print("\n--- Typumwandlungen ---")
print(f"Casting float 3.99 zu int: {int(3.99)}") # Abschneiden, nicht runden!

# String zu Zahl (Essentiell für Benutzereingaben)
strom_str = "0.5"
strom_float = float(strom_str)
print(f"Berechnung: {strom_float * 2} A")

# Truthiness-Logik (Konvertierung nach bool)
print(f"int 0 zu bool:   {bool(0)}")      # False
print(f"int 42 zu bool:  {bool(42)}")     # True
print(f"str '' zu bool:  {bool('')}")     # False (leerer String)
print(f"None zu bool:    {bool(None)}")   # False

# Spezialfälle nach int
print(f"bool True zu int: {int(True)}")   # 1
print(f"bool False zu int: {int(False)}") # 0


# ==========================================
# Aufgabe 5 & 6: Kollektionen & Dictionaries
# ==========================================

print("\n--- Dictionaries & Listen ---")

# Initialisierung leeres Dict
mydict = {"Name": None, "Alter": None, "Geschlecht": None}
print(f"Dictionary: {mydict}, Typ: {type(mydict)}")

# Werte zuweisen
mydict["Name"] = "Hans"
mydict["Alter"] = 21
mydict["Geschlecht"] = "m"

print(f"Alle Werte: {mydict.values()}")

# Anwendung in/not in
if "Alter" in mydict:
    print(f"Das Alter von {mydict['Name']} ist bekannt.")

if "Gewicht" not in mydict:
    print("Die Information 'Gewicht' fehlt im Dictionary.")

# Zweites Dictionary
mydict2 = {"Name": "Stefanie", "Alter": 20, "Geschlecht": "w"}

# Liste von Dicts
mylist = [mydict, mydict2]
print(f"Meine Liste: {mylist}")

# Extra Key-Value-Paar hinzufügen
mydict["Stadt"] = "Ingolstadt"
mydict2["Stadt"] = "Eichstätt"

print(f"Finale Liste: {mylist}")
