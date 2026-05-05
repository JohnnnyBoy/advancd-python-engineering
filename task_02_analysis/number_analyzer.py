import math

def ist_primzahl(n):
    """Prüft, ob n eine Primzahl ist."""
    assert isinstance(n, int) and n > 1, "Zahl muss ein Integer > 1 sein."
    if n == 2: return True
    if n % 2 == 0: return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def ist_armstrong(n):
    """Prüft, ob n eine Armstrong-Zahl ist."""
    assert isinstance(n, int) and n >= 0, "Zahl muss eine positive ganze Zahl sein."
    
    s_n = str(n)
    anzahl_ziffern = len(s_n)
    summe = sum(int(ziffer) ** anzahl_ziffern for ziffer in s_n)
    
    return summe == n

def ist_perfekt(n):
    """Prüft, ob n eine perfekte Zahl ist."""
    assert isinstance(n, int) and n > 0, "Zahl muss eine positive ganze Zahl > 0 sein."
    
    summe_teiler = 0
    for i in range(1, n):
        if n % i == 0:
            summe_teiler += i
            
    return summe_teiler == n

def main():
    while True:
        print("\n- Zahlen-Analyse-Tool -")
        print("Verfügbare Analysen: [prime] | [armstrong] | [perfect] | [exit]")
        
        wahl = input("Wahl treffen: ").strip().lower()
        
        if wahl == "exit":
            print("Programm beendet. Bis zum nächsten Mal!")
            break
            
        if wahl not in ["prime", "armstrong", "perfect"]:
            print("Fehler: Ungültiger Analyse-Typ!")
            continue

        try:
            zahl_input = input(f"Welche Zahl soll auf '{wahl}' geprüft werden? ")
            zahl = int(zahl_input)
            
            ergebnis = False
            if wahl == "prime":
                ergebnis = ist_primzahl(zahl)
            elif wahl == "armstrong":
                ergebnis = ist_armstrong(zahl)
            elif wahl == "perfect":
                ergebnis = ist_perfekt(zahl)

            # Ausgabe
            status = "ist eine" if ergebnis else "ist KEINE"
            print(f" Ergebnis: Die Zahl {zahl} {status} {wahl.capitalize()}-Zahl.")

        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Ganzzahl ein.")
        except AssertionError as e:
            print(f"Validierungsfehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
