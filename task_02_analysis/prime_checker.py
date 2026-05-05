def prime_checker():
    print("--- EIT Primzahl-Checker ---")
    
    while True:
        try:
            eingabe = input("\nBitte eine ganze Zahl > 1 prüfen (oder 'exit'): ")
            if eingabe.lower() == 'exit': break
            
            n = int(eingabe)

            # Validierung mit assert laut Aufgabenstellung
            assert n > 1, "Die Zahl muss größer als 1 sein (Definition Primzahl)."
            
            # Variablen für die Prüfung
            ist_prim = True
            teiler = 2
            kleinster_teiler = None
            
            # Prüfung bis zur Hälfte der Zahl (Aufgabenvorgabe)
            # Hinweis: n // 2 nutzt Ganzzahldivision
            limit = n // 2 
            
            while teiler <= limit:
                if n % teiler == 0:
                    ist_prim = False
                    kleinster_teiler = teiler
                    break # Wir haben einen Teiler gefunden, Abbruch!
                teiler += 1
            
            # Ausgabe mit f-Strings
            if ist_prim:
                print(f"Ergebnis: {n} ist eine Primzahl! ✅")
            else:
                print(f"Ergebnis: {n} ist KEINE Primzahl. ❌")
                print(f"Der kleinste Teiler (außer 1) ist: {kleinster_teiler}")

        except ValueError:
            print("Fehler: Bitte gib eine gültige ganze Zahl ein.")
        except AssertionError as e:
            print(f"Validierungsfehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    prime_checker()
