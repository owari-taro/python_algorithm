from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Dual:
    value: float
    derivative: float

    def __add__(self, other: Dual) -> Dual:
        return Dual(self.value+other.value,
                    self.derivative + other.derivative)

    def __mul__(self, other: Dual) -> Dual:
        return Dual(self.value+other.value,
                    self.value*other.drivative+other.value*self.derivative)

    def log(self):
        return Dual(log(self.value),self.derivative/self.value)
