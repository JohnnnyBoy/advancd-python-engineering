def calculate_next(actual_number: str) -> str:
    # calculation with str -> int -> str ...
    # validation: str is int and (is not None or str)
    n = actual_number
    assert type(n) in [str, int] and int(n) >= 0, "Eingabe muss ein Ziffern-String sein."

    # alternativ über isinstance und actual_number.isdigit(): 
    # assert isinstance(actual_number, str) and actual_number.isdigit(), "Eingabe muss ein Ziffern-String sein."

    result_str = "" # None += None -> TypeError # 0 += str -> TypeError
    # if actual_number == None: return None

    zaehler = 1 #1 = 1. number, None = 0. number
    # iteration: len(str) <-> actual sign
    for i in range(len(actual_number)):
        # check is there a next sign AND # is it the same sign
        if i + 1 < len(actual_number) and (actual_number[i] == actual_number[i + 1]):
            zaehler += 1
        else:
            # Hier "beschreiben" wir: Anzahl + Ziffer
            result_str += str(zaehler) + actual_number[i]   # bsp. 3x1 -> result_str = 3+1 = '31'
            zaehler = 1                                     # zaehler ready for next sign

    return result_str

def conway10(initial_value) -> str:
    # conway for 10 steps # error for valueerror
    try:
        # Validierung und Vorbereitung
        initial_str = str(initial_value)        # check again: is input: +int?
        assert initial_str.isdigit() and int(initial_str) > 0, f"Fehler: {initial_value} ist keine positive ganze Zahl."
        # alternativ:
        # if not initial_str.isdigit() or int(initial_str) <= 0: 
        #     return f"Fehler: {initial_value} ist keine positive ganze Zahl."

        # first output is start value, then 10 steps
        entire_output = ""
        actual_value = initial_str
        entire_output += f" 0: {actual_value}"
        
        # 10 Schritte berechnen
        for step in range(1, 11):
            actual_value = calculate_next(actual_value)
            prefix = " " if step < 10 else ""
            entire_output += f"\n{prefix}{step}: {actual_value}"
        return entire_output

    except AssertionError as e:         # return, because I need str output in error case
        return str(e)
    except Exception as e:
        return str(e)

def main():
    while True:
        print("\n- Conway-Sequence (Look-and-Say) -")
        user_input = input("Gib eine positive Startzahl ein (oder 'q' zum Beenden): ").strip()
        
        # .strip(): prevent ' '/'\t'/'\n'
        # .lower(): prevent 'Q'->'q' # .upper(): prevent 'q'->'Q'
        if user_input.lower() == 'q':       # early exit
            print("Programm wird beendet.")
            break
            
        try:
            # Aufruf der conway10 Funktion
            print("\n" + conway10(user_input))
            
        except ValueError:
            print("Fehler: Bitte gib eine gültige Ganzzahl ein.")
        except Exception as e:
            print(f"Fehler in der Verarbeitung: {e}")

if __name__ == "__main__":
    main()
