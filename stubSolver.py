import cmath
from typing import Optional


class stubSolver:
    def __init__(self, real: float, fake: float, z0real: float, z0fake: float,
                 beta: float, gamma: complex, length: float, short: Optional[bool]):
        
        self.Z0 = complex(z0real, z0fake)
        self.load = complex(real, fake)
        self.beta = beta
        self.gamma = gamma if gamma is not None else 1j * beta
        self.length = length
        self.short = short

    def input_impedance(self):
        tanh_gl = cmath.tanh(self.gamma * self.length)

        if self.short is True:
            # ZL = 0 special case: Zin = Z0 * tanh(gamma*l)
            return self.Z0 * tanh_gl
        elif self.short is False:
            # ZL -> infinity special case: Zin = Z0 / tanh(gamma*l)
            return self.Z0 / tanh_gl
        else:
            # General terminated line: Zin = Z0 * (ZL + Z0*tanh(gl)) / (Z0 + ZL*tanh(gl))
            ZL = self.load
            return self.Z0 * (ZL + self.Z0 * tanh_gl) / (self.Z0 + ZL * tanh_gl)

    def input_reactance(self):
        return self.input_impedance().imag


if __name__ == "__main__":
    beta = 1.0
    length = 0.125
    Z0 = 50.0

    short_stub = stubSolver(real=0, fake=0, z0real=Z0, z0fake=0,
                             beta=beta, gamma=1j * beta, length=length, short=True)
    open_stub = stubSolver(real=0, fake=0, z0real=Z0, z0fake=0,
                            beta=beta, gamma=1j * beta, length=length, short=False)
    general_stub = stubSolver(real=75, fake=-30, z0real=Z0, z0fake=0,
                               beta=beta, gamma=1j * beta, length=length, short=None)

    print("Short-circuit stub Zin:", short_stub.input_impedance())
    print("Open-circuit stub Zin:", open_stub.input_impedance())
    print("General ZL=75-30j stub Zin:", general_stub.input_impedance())