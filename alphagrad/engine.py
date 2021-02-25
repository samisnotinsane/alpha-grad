from __future__ import annotations
import math

class Dual:
    def __init__(self, real, dual):
        self.r = real
        self.d = dual

    def __str__(self):
        pass

    def __add__(self, other: Dual) -> Dual:
        pass

    def __sub__(self, other: Dual) -> Dual:
        pass

    def __mul__(self, other: Dual) -> Dual:
        pass

    def __truediv__(self, other: Dual) -> Dual:
        pass

    def __pow__(self, other: Dual) -> Dual:
        pass

    def sin(x: Dual) -> Dual:
        return Dual(math.sin(x.r), math.cos(x.r)*x.d)

    def cos(x: Dual) -> Dual:
        return Dual(math.cos(x.r), -math.sin(x.r)*x.d)
    
    def tan(x: Dual) -> Dual:
        return Dual(math.tan(x.r), (x.d/math.cos(x.r))**2 )

    def exp(x: Dual) -> Dual:
        return Dual(math.exp(x.r), math.exp(x.r)*x.d)
