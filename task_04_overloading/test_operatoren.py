import operatoren as op

# --------------------------------------------------------
# Tests __str__
def test_str( v1, v2, s1, s2):

    success = True

    v1_str = str(v1)
    if( v1_str == "( 1.00, 2.00, 3.00)"):
        print("Ergebnis korrekt: String-Methode für Vektor3D")
    else:
        print("*** Fehler: String-Methode für Vektor3D nicht korrekt. Bitte prüfen Sie die Formatierung!")
        print("str(v1): Erwartet:    '( 1.00, 2.00, 3.00)'")
        print("         Tatsächlich: '" + v1_str + "'")
        success = False

    s1_str = str(s1)
    if( s1_str == "3.50"):
        print("Ergebnis korrekt: String-Methode für Skalar")
    else:
        print("*** Fehler: String-Methode für Skalar nicht korrekt. Bitte prüfen Sie die Formatierung!")
        print("str(s1): Erwartet:    '3.50'")
        print("         Tatsächlich: '" + s1_str + "'")
        success = False

    print()
    return success


# --------------------------------------------------------
# Tests __eq__
def test_eq( v1, v2, s1, s2):

    success = True

    v1_eq = op.Vektor3D( 1, 2, 3 )
    if( v1_eq == v1 and not( v2 == v1) ):
        print("Ergebnis korrekt: Gleichheit von Vektor3D-Objekten")
    else:
        print("*** Fehler: Gleichheit von Vektor3D-Objekten nicht korrekt.")
        print("Erwartet:    ( 1.00, 2.00, 3.00) == ( 1.00, 2.00, 3.00); ( 1.00, 2.00, 3.00) != ( 4.10, 5.20, 6.30)")
        conn1 = "!="
        if( v1_eq == v1):
            conn1 = "=="
        conn2 = "!="
        if( v2 == v1):
            conn2 = "=="
        print("Tatsächlich: ( 1.00, 2.00, 3.00) " + conn1 + " ( 1.00, 2.00, 3.00); ( 1.00, 2.00, 3.00) " + conn2 + " ( 4.10, 5.20, 6.30)")
        success = False

    s1_eq = op.Skalar( 3.5)
    if( s1_eq == s1 and not( s1 == s2 )):
        print("Ergebnis korrekt: Gleichheit von Skalar-Objekten")
    else:
        print("*** Fehler: Gleichheit von Skalar-Objekten nicht korrekt.")
        print("Erwartet:    3.50 == 3.50; 3.50 != 7.00")
        conn1 = "!="
        if( s1_eq == s1):
            conn1 = "=="
        conn2 = "!="
        if( s2 == s1):
            conn2 = "=="
        print("Tatsächlich: 3.50 " + conn1 + " 3.50; 3.50 " + conn2 + " 7.00")
        success = False

    print()
    return success


# --------------------------------------------------------
# Tests __add__
def test_add( v1, v2, s1, s2):

    success = True

    v_add = str(v1 + v2)
    if( v_add == "( 5.10, 7.20, 9.30)"):
        print("Ergebnis korrekt: Addition von zwei Vektor3D-Objekten")
    else:
        print("*** Fehler: Addition von zwei Vektor3D-Objekten nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("v1 + v2: Erwartet:    ( 5.10, 7.20, 9.30)")
        print("         Tatsächlich: " + v_add )
        print()
        success = False

    s_add = str(s1 + s2)
    if( s_add == "10.50"):
        print("Ergebnis korrekt: Addition von zwei Skalar-Objekten")
    else:
        print("*** Fehler: Addition von zwei Skalar-Objekten nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("s1 + s2: Erwartet:    10.50")
        print("         Tatsächlich: " + s_add )
        print()
        success = False

    try:
        add_err = v1 + 1
        print("*** Fehler: Der Versuch, ein Nicht-Vektor3D-Objekt zu einem Vektor3D-Objekt zu addieren, führt NICHT zu einer Exception!")
        print()
        success = False
    except TypeError: # Type-Error erwartet
        print( "Ergebnis korrekt: Der Versuch, ein Nicht-Vektor3D-Objekt zu einem Vektor3D-Objekt zu addieren, ergibt einen TypeError")
    except Exception as ex: # anderer Error-Typ: Fehler
        print()
        print("*** Fehler: Der Versuch, ein Nicht-Vektor3D-Objekt zu einem Vektor3D-Objekt zu addieren, ergibt FALSCHEN Error-Typ!")
        print("Erwartet:    TypeError")
        print("Tatsächlich: " + type(ex).__name__ )
        success = False
        print()

    try:
        add_err = s1 + 5
        print("*** Fehler: Der Versuch, ein Nicht-Skalar-Objekt zu einem Skalar-Objekt zu addieren, führt NICHT zu einer Exception!")
        print()
        success = False
    except TypeError: # Type-Error erwartet
        print( "Ergebnis korrekt: Der Versuch, ein Nicht-Skalar-Objekt zu einem Skalar-Objekt zu addieren, ergibt einen TypeError")
    except Exception as ex: # anderer Error-Typ: Fehler
        print()
        print("*** Fehler: Der Versuch, ein Nicht-Skalar-Objekt zu einem Skalar-Objekt zu addieren, ergibt FALSCHEN Error-Typ!")
        print("Erwartet:    TypeError")
        print("Tatsächlich: " + type(ex).__name__ )
        print()
        success = False

    print()
    return success


# --------------------------------------------------------
# Tests __sub__
def test_sub( v1, v2, s1, s2):

    success = True

    v_sub = str(v1 - v2)
    if( v_sub == "( -3.10, -3.20, -3.30)"):
        print("Ergebnis korrekt: Subtraktion von zwei Vektor3D-Objekten")
    else:
        print("*** Fehler: Subtraktion von zwei Vektor3D-Objekten nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("v1 - v2: Erwartet:    ( -3.10, -3.20, -3.30)")
        print("         Tatsächlich: " + v_sub )
        print()
        success = False

    s_sub = str(s1 - s2)
    if( s_sub == "-3.50"):
        print("Ergebnis korrekt: Subtraktion von zwei Skalar-Objekten")
    else:
        print("*** Fehler: Subtraktion von zwei Skalar-Objekten nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("s1 - s2: Erwartet:    -3.50")
        print("         Tatsächlich: " + s_sub )
        print()
        success = False

    try:
        sub_err = v1 - 1
        print("*** Fehler: Der Versuch, ein Nicht-Vektor3D-Objekt von einem Vektor3D-Objekt zu subtrahieren, führt NICHT zu einer Exception!")
        print()
        success = False
    except TypeError: # Type-Error erwartet
        print( "Ergebnis korrekt: Der Versuch, ein Nicht-Vektor3D-Objekt von einem Vektor3D-Objekt zu subtrahieren, ergibt einen TypeError")
    except Exception as ex: # anderer Error-Typ: Fehler
        print()
        print("*** Fehler: Der Versuch, ein Nicht-Vektor3D-Objekt von einem Vektor3D-Objekt zu subtrahieren, ergibt FALSCHEN Error-Typ!")
        print("Erwartet:    TypeError")
        print("Tatsächlich: " + type(ex).__name__ )
        print()
        success = False

    try:
        sub_err = s1 - 5
        print("*** Fehler: Der Versuch, ein Nicht-Skalar-Objekt von einem Skalar-Objekt zu subtrahieren, führt NICHT zu einer Exception!")
        print()
        success = False
    except TypeError: # Type-Error erwartet
        print( "Ergebnis korrekt: Der Versuch, ein Nicht-Skalar-Objekt von einem Skalar-Objekt zu subtrahieren, ergibt einen TypeError")
    except Exception as ex: # anderer Error-Typ: Fehler
        print()
        print("*** Fehler: Der Versuch, ein Nicht-Skalar-Objekt von einem Skalar-Objekt zu subtrahieren, ergibt FALSCHEN Error-Typ!")
        print("Erwartet:    TypeError")
        print("Tatsächlich: " + type(ex).__name__ )
        print()
        success = False

    print()
    return success


# --------------------------------------------------------
# Tests __mul__
def test_mul( v1, v2, s1, s2):
# v1 * v2 = 33.40 , v1 * s1 = ( 3.50, 7.00, 10.50)
# s1 * s2 = 24.50 , s1 * v1 = ( 3.50, 7.00, 10.50)

    success = True

    vv_mul = str(v1 * v2)
    if( vv_mul == "33.40"):
        print("Ergebnis korrekt: Multiplikation von zwei Vektor3D-Objekten")
    else:
        print("*** Fehler: Multiplikation von zwei Vektor3D-Objekten nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("v1 * v2: Erwartet:    33.40")
        print("         Tatsächlich: " + vv_mul )
        print()
        success = False

    sv_mul = str(s1 * v1)
    if( sv_mul == "( 3.50, 7.00, 10.50)"):
        print("Ergebnis korrekt: Multiplikation von Skalar-Objekt mit Vektor3D-Objekt")
    else:
        print("*** Fehler: Multiplikation von Skalar-Objekt mit Vektor3D-Objekt nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("s1 * v1: Erwartet:    '( 3.50, 7.00, 10.50)'")
        print("         Tatsächlich: '" + sv_mul + "'")
        print()
        success = False

    vs_mul = str(v1 * s1)
    if( vs_mul == "( 3.50, 7.00, 10.50)"):
        print("Ergebnis korrekt: Multiplikation von Vektor3D-Objekt mit Skalar-Objekt")
    else:
        print("*** Fehler: Multiplikation von Vektor3D-Objekt mit Skalar-Objekt nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("v1 * s1: Erwartet:    '( 3.50, 7.00, 10.50)'")
        print("         Tatsächlich: '" + vs_mul + "'")
        print()
        success = False

    ss_mul = str(s1 * s2)
    if( ss_mul == "24.50"):
        print("Ergebnis korrekt: Multiplikation von zwei Skalar-Objekten")
    else:
        print("*** Fehler: Multiplikation von zwei Skalar-Objekten nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("s1 * s2: Erwartet:    24.50")
        print("         Tatsächlich: " + ss_mul )
        print()
        success = False

    try:
        mul_err = v1 * 1
        print("*** Fehler: Der Versuch, ein Objekt, das weder vom Typ Skalar noch vom Typ Vektor3D ist, mit einem Vektor3D-Objekt zu multiplizieren, führt NICHT zu einer Exception!")
        print()
        success = False
    except TypeError: # Type-Error erwartet
        print( "Ergebnis korrekt: Der Versuch, ein Objekt, das weder vom Typ Skalar noch vom Typ Vektor3D ist, mit einem Vektor3D-Objekt zu multiplizieren, ergibt einen TypeError")
    except Exception as ex: # anderer Error-Typ: Fehler
        print()
        print("*** Fehler: Der Versuch, ein Objekt, das weder vom Typ Skalar noch vom Typ Vektor3D ist, mit einem Vektor3D-Objekt zu multiplizieren, ergibt FALSCHEN Error-Typ!")
        print("Erwartet:    TypeError")
        print("Tatsächlich: " + type(ex).__name__ )
        print()
        success = False

    try:
        mul_err = s1 * 1
        print("*** Fehler: Der Versuch, ein Objekt, das weder vom Typ Skalar noch vom Typ Vektor3D ist, mit einem Skalar-Objekt zu multiplizieren, führt NICHT zu einer Exception!")
        print()
        success = False
    except TypeError: # Type-Error erwartet
        print( "Ergebnis korrekt: Der Versuch, ein Objekt, das weder vom Typ Skalar noch vom Typ Vektor3D ist, mit einem Skalar-Objekt zu multiplizieren, ergibt einen TypeError")
    except Exception as ex: # anderer Error-Typ: Fehler
        print()
        print("*** Fehler: Der Versuch, ein Objekt, das weder vom Typ Skalar noch vom Typ Vektor3D ist, mit einem Skalar-Objekt zu multiplizieren, ergibt FALSCHEN Error-Typ!")
        print("Erwartet:    TypeError")
        print("Tatsächlich: " + type(ex).__name__ )
        print()
        success = False

    print()
    return success


# --------------------------------------------------------
# Tests __truediv__
def test_div( v1, v2, s1, s2):
# s1 / s2 = 0.50 , v1 / s1 = ( 0.29, 0.57, 0.86)

    success = True

    v_div = str(v1 / s1)
    if( v_div == "( 0.29, 0.57, 0.86)"):
        print("Ergebnis korrekt: Division von Vektor3D-Objekt durch Skalar-Objekt")
    else:
        print("*** Fehler: Division von Vektor3D-Objekt durch Skalar-Objekt nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("v1 / v2: Erwartet:    ( 0.29, 0.57, 0.86)")
        print("         Tatsächlich: " + v_div )
        print()
        success = False

    s_div = str(s1 / s2)
    if( s_div == "0.50"):
        print("Ergebnis korrekt: Division von Skalar-Objekt durch Skalar-Objekt")
    else:
        print("*** Fehler: Division von Skalar-Objekt durch Skalar-Objekt nicht korrekt. Bitte prüfen Sie Ihre Methode!")
        print("s1 / s2: Erwartet:    0.50")
        print("         Tatsächlich: " + s_div )
        print()
        success = False

    try:
        div_err = v1 / 1
        print("*** Fehler: Der Versuch, ein Vektor3D-Objekt durch ein Nicht-Skalar-Objekt zu dividieren, führt NICHT zu einer Exception!")
        print()
        success = False
    except TypeError: # Type-Error erwartet
        print( "Ergebnis korrekt: Der Versuch, ein Vektor3D-Objekt durch ein Nicht-Skalar-Objekt zu dividieren, ergibt einen TypeError")
    except Exception as ex: # anderer Error-Typ: Fehler
        print()
        print("*** Fehler: Der Versuch, ein Vektor3D-Objekt durch ein Nicht-Skalar-Objekt zu dividieren, ergibt FALSCHEN Error-Typ!")
        print("Erwartet:    TypeError")
        print("Tatsächlich: " + type(ex).__name__ )
        print()
        success = False

    try:
        div_err = s1 / 1
        print("*** Fehler: Der Versuch, ein Skalar-Objekt durch ein Nicht-Skalar-Objekt zu dividieren, führt NICHT zu einer Exception!")
        print()
        success = False
    except TypeError: # Type-Error erwartet
        print( "Ergebnis korrekt: Der Versuch, ein Skalar-Objekt durch ein Nicht-Skalar-Objekt zu dividieren, ergibt einen TypeError")
    except Exception as ex: # anderer Error-Typ: Fehler
        print()
        print("*** Fehler: Der Versuch, ein Skalar-Objekt durch ein Nicht-Skalar-Objekt zu dividieren, ergibt FALSCHEN Error-Typ!")
        print("Erwartet:    TypeError")
        print("Tatsächlich: " + type(ex).__name__ )
        success = False
        print()

    print()
    return success




# =========================================================
def main():
    v1 = op.Vektor3D( 1, 2, 3 )
    v2 = op.Vektor3D( 4.1, 5.2, 6.3)

    s1 = op.Skalar( 3.5)
    s2 = op.Skalar( 7.0)

    print()
    print("Verwendete Test-Werte:")
    print("======================")
    print("v1 =", v1)
    print("v2 =", v2)
    print("s1 =", s1, ", s2 =", s2)
    print()
    anz_tests = 8

    # --------------------------------------------------------
    # Tests __str__
    print("Test: __str__-Methoden:")
    print("=======================")
    if( not test_str( v1, v2, s1, s2)):
        print("Test abgebrochen nach Test 1 von", anz_tests)
        print()
        return

    # --------------------------------------------------------
    # Tests __eq__
    print("Test: Überladen von '==' -> __eq__-Methoden:")
    print("============================================")
    if( not test_eq( v1, v2, s1, s2)):
        print("Test abgebrochen nach Test 2 von", anz_tests)
        print()
        return

    # --------------------------------------------------------
    # Tests __add__
    print("Test: Überladen von '+' -> __add__-Methoden:")
    print("============================================")
    if( not test_add( v1, v2, s1, s2)):
        print("Test abgebrochen nach Test 3 von", anz_tests)
        print()
        return

    # --------------------------------------------------------
    # Tests __sub__
    print("Test: Überladen von '-' -> __sub__-Methoden:")
    print("============================================")
    if( not test_sub( v1, v2, s1, s2)):
        print("Test abgebrochen nach Test 4 von", anz_tests)
        print()
        return

    # --------------------------------------------------------
    # Tests __mul__
    print("Test: Überladen von '*' -> __mul__-Methoden:")
    print("============================================")
    if( not test_mul( v1, v2, s1, s2)):
        print("Test abgebrochen nach Test 5 von", anz_tests)
        print()
        return

    # --------------------------------------------------------
    # Tests __truediv__
    print("Test: Überladen von '/' -> __truediv__-Methoden:")
    print("================================================")
    if( not test_div( v1, v2, s1, s2)):
        print("Test abgebrochen nach Test 6 von", anz_tests)
        print()
        return



    print()


#=========================================================================
# Standard-Footer
if( __name__ == '__main__'):
    main()
