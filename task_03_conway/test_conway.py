import conway_main as conway

def main():
    test_dict = {"1": " 0: 1\n 1: 11\n 2: 21\n 3: 1211\n 4: 111221\n 5: 312211\n 6: 13112221\n 7: 1113213211\n 8: 31131211131221\n 9: 13211311123113112211\n10: 11131221133112132113212221",
                "5555": " 0: 5555\n 1: 45\n 2: 1415\n 3: 11141115\n 4: 31143115\n 5: 132114132115\n 6: 11131221141113122115\n 7: 311311222114311311222115\n 8: 1321132132211413211321322115\n 9: 11131221131211132221141113122113121113222115\n10: 3113112221131112311332211431131122211311123113322115",
                123: " 0: 123\n 1: 111213\n 2: 31121113\n 3: 1321123113\n 4: 1113122112132113\n 5: 3113112221121113122113\n 6: 13211321322112311311222113\n 7: 111312211312111322211213211321322113\n 8: 311311222113111231133221121113122113121113222113\n 9: 13211321322113311213212322211231131122211311123113322113\n10: 11131221131211132221232112111312111213322112132113213221133112132123222113",
                "abc": "Fehler: abc ist keine positive ganze Zahl.",
                1.5: "Fehler: 1.5 ist keine positive ganze Zahl.",
                -20:  "Fehler: -20 ist keine positive ganze Zahl."}

    # Zähler, damit Anzahl bestandener Tests ausgegeben werden kann
    test_nr = 0

    # Testfälle durchlaufen
    for key in test_dict:
        test_nr += 1
        con = conway.conway10(key)

        # Version des Keys für die Ausgabe, damit String- und Int-Input unterschieden werden kann
        key_print = key
        if( isinstance( key, str)):
            key_print = "\"" + key + "\""
        if( con == test_dict[key]):
            print( "Ergebnis korrekt: conway10(", key_print, ")")
        else:
            print()
            print( "FEHLER: conway10(", key_print, ") ist NICHT korrekt.")
            print()
            print( "Bitte prüfen Sie, ob Ihre Formatierung _exakt_ stimmt! Prüfen Sie insbesondere die Einrückung, und ob an der letzten Zeile auch sicher kein Zeilenumbruch mehr hängt.")
            print()
            print( "Erwartet:")
            print( test_dict[key])
            print("Tatsächlich:")
            print( con)
            print( "Ausführung nach Test", test_nr, "von 5 abgebrochen.")
            print()
            return
            


# Standard-Footer: main() nur aufrufen, falls Skript nicht importiert
if(__name__ == '__main__'):
    main()
