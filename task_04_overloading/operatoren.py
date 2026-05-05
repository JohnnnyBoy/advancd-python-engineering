class Skalar:
    # s1 = Skalar(5) -> s1.wert = 5.0 (1. Object)
    def __init__(self, wert):
        # check value of wert to int, float
        assert isinstance(wert, (int, float)), "Skalar-Wert muss eine Zahl sein."
        self.wert = float(wert)

    def __str__(self):
        # Ausgabe mit 2 Nachkommastellen
        return f"{self.wert:.2f}"

    def __eq__(self, other):
        if isinstance(other, Skalar):
            return self.wert == other.wert
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Skalar):
            return Skalar(self.wert + other.wert)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Skalar):
            return Skalar(self.wert - other.wert)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Skalar):
            return Skalar(self.wert * other.wert)
        if isinstance(other, Vektor3D):
            # Skalar * Vektor = Vektor
            return Vektor3D(self.wert * other.x, self.wert * other.y, self.wert * other.z)
        return NotImplemented

    def __truediv__(self, other):
        # Skalar / Skalar = Skalar
        if isinstance(other, Skalar):
            assert other.wert != 0, "Division durch Null nicht möglich."
            return Skalar(self.wert / other.wert)
        # Skalar / Vektor = NotImplemented
        return NotImplemented


class Vektor3D:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)), "x muss eine Zahl sein."
        assert isinstance(y, (int, float)), "y muss eine Zahl sein."
        assert isinstance(z, (int, float)), "z muss eine Zahl sein."
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        # Format: ( 1.10, 2.20, 3.30)
        return f"( {self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __eq__(self, other):
        if isinstance(other, Vektor3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vektor3D):
            return Vektor3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vektor3D):
            return Vektor3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Skalar):
            # Vektor * Skalar
            return Vektor3D(self.x * other.wert, self.y * other.wert, self.z * other.wert)
        if isinstance(other, Vektor3D):
            # Skalarprodukt: x1*x2 + y1*y2 + z1*z2
            ergebnis = (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
            return Skalar(ergebnis)
        return NotImplemented

    def __truediv__(self, other):
        # Nur Division durch Skalar erlaubt
        if isinstance(other, Skalar):
            assert other.wert != 0, "Division durch Null nicht möglich."
            return Vektor3D(self.x / other.wert, self.y / other.wert, self.z / other.wert)
        return NotImplemented

def main():
    try:
        # 1. Test: Konstruktoren und str
        s1 = Skalar(5)
        v1 = Vektor3D(1, 2, 3)
        print(f"Skalar s1: {s1}")
        print(f"Vektor v1: {v1}")

        # 2. Test: Addition / Subtraktion
        v2 = Vektor3D(10, 10, 10)
        print(f"v1 + v2: {v1 + v2}")
        
        # 3. Test: Multiplikation (Vektor * Skalar und Skalarprodukt)
        print(f"v1 * s1: {v1 * s1}")
        print(f"v1 * v2: {v1 * v2} (Skalarprodukt)")

        # 4. Test: Division
        print(f"v2 / s1: {v2 / s1}")

        # 5. Test: Exception Provokation
        print("\nTest Fehlerszenario (Skalar / Vektor):")
        # NotImplemented -> TypeError
        result = s1 / v1 

    except TypeError:
        print("Abgefangen: Operation zwischen diesen Typen nicht unterstützt (wie erwartet).")
    except AssertionError as e:
        print(f"Validierungsfehler: {e}")
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")

if __name__ == "__main__":
    main()
