def temperature_konverter():
    print("- Temperature-Konverter (Celsius, Kelvin, Fahrenheit) -")
    print("Tippe 'exit' bei der Einheit, um das Programm zu beenden.")

    while True:
        try:
            # 1. Eingabe
            eingabe_wert = input("\nTemperaturwert eingeben: ")
            if eingabe_wert.lower() == 'exit': break
            
            wert = float(eingabe_wert)
            einheit = input("Einheit (C, K, F): ").strip().upper()
            if einheit == 'EXIT': break

            # Variablen mit assert prüfen
            assert einheit in ['C', 'K', 'F'], "Ungültige Einheit! Bitte C, K oder F nutzen."

            # 2. Berechnung & Logik
            if einheit == 'C':
                celsius = wert
                kelvin = celsius + 273.15
                fahrenheit = (celsius * 9/5) + 32
            elif einheit == 'K':
                kelvin = wert
                celsius = kelvin - 273.15
                fahrenheit = (celsius * 9/5) + 32
            elif einheit == 'F':
                fahrenheit = wert
                celsius = (fahrenheit - 32) * 5/9
                kelvin = celsius + 273.15

            # Assert: Physikalisches Limit prüfen (Absoluter Nullpunkt)
            assert kelvin >= 0, f"Physikalisch unmöglich! {kelvin}K liegt unter dem absoluten Nullpunkt."

            # 3. Ausgabe mit f-Strings
            print(f"--- Ergebnisse für {wert} {einheit} ---")
            print(f"Celsius:    {celsius:8.2f} °C")
            print(f"Kelvin:     {kelvin:8.2f} K")
            print(f"Fahrenheit: {fahrenheit:8.2f} °F")

        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl für die Temperatur ein.")
        except AssertionError as e:
            print(f"Validierungsfehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    temperature_konverter()
