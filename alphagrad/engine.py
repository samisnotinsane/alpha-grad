from __future__ import annotations
import math

class Dual:
    def __init__(self, real, dual):
        """
        dual.r -> real,
        dual.d -> dual
        """
        self.r = real
        self.d = dual

    def __str__(self):
        return str(self.r) + " + " + str(self.d) + "ε"

    def __add__(self, other: Dual) -> Dual:
        """
        Computes Dual(a + b, da + db),
        where,
        da = self.dual,
        db = other.dual
        """
        return Dual(self.r + other.r, self.d + other.d)

    def __sub__(self, other: Dual) -> Dual:
        """
        Computes Dual(a - b, da - db),
        where,
        da = self.dual,
        db = other.dual
        and a, b is self.real, other.real
        """
        return Dual(self.r - other.r, self.d - other.d)

    def __mul__(self, other: Dual) -> Dual:
        """
        Computes Dual(a*b, b*da + a*db)
        where,
        da = self.dual
        db = other.dual
        and a, b is self.real, other.real
        """
        return Dual(self.r * other.r, other.r * self.d + self.r * other.d)

    def __truediv__(self, other: Dual) -> Dual:
        """
        Computes Dual(a/b, da/b-a*db/b**2)
        where,
        da = self.dual
        db = other.dual
        and a, b is self.real, other.real
        """
        return Dual(self.r / other.r, ((self.d / other.r) - (self.r * other.d)) / other.r**2)

    def __pow__(self, other: Dual) -> Dual:
        return Dual(other.r * self.r**(other.r-1) * self.d + math.log(self.r) * self.r**other.r * other.d)

    def sin(x: Dual) -> Dual:
        return Dual(math.sin(x.r), math.cos(x.r)*x.d)

    def cos(x: Dual) -> Dual:
        return Dual(math.cos(x.r), -math.sin(x.r)*x.d)
    
    def tan(x: Dual) -> Dual:
        return Dual(math.tan(x.r), (x.d/math.cos(x.r))**2 )

    def exp(x: Dual) -> Dual:
        return Dual(math.exp(x.r), math.exp(x.r)*x.d)
