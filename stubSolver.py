import cmath
from typing import Optional


class stubSolver:
    def __init__(self, real: float, fake: float, z0real: float, z0fake: float,
                 beta: float, alpha: float, gamma: Optional[complex] = None,
                 length: Optional[float] = None, short: Optional[bool] = None):
        self.Z0 = complex(z0real, z0fake)
        self.load = complex(real, fake)
        self.beta = beta
        self.alpha = alpha
        self.gamma = gamma if gamma is not None else complex(alpha, beta)
        self.length = length
        self.short = short

    def input_impedance(self, length: Optional[float] = None):
        l = length if length is not None else self.length
        if l is None:
            raise ValueError("length must be supplied at init or passed to input_impedance()")

        tanh_gl = cmath.tanh(self.gamma * l)

        if self.short is True:
            return self.Z0 * tanh_gl
        elif self.short is False:
            return self.Z0 / tanh_gl
        else:
            ZL = self.load
            return self.Z0 * (ZL + self.Z0 * tanh_gl) / (self.Z0 + ZL * tanh_gl)

    def input_reactance(self, length: Optional[float] = None):
        return self.input_impedance(length).imag

    def required_length(self, target_impedance: complex):

        if self.short is None:
            raise ValueError("required_length() only applies to short (True) or open (False) stubs")

        Z0 = self.Z0
        if self.short:
            arg = target_impedance / Z0
        else:
            arg = Z0 / target_impedance

        gl = cmath.atanh(arg)

        lossy_gamma = self.gamma
        lossless_gamma = 1j * self.beta

        lossy_length = (gl / lossy_gamma).real
        lossless_length = (gl / lossless_gamma).real

        delta_length = lossy_length - lossless_length
        return lossy_length, lossless_length, delta_length


if __name__ == "__main__":
    beta = 1.0     # rad/m
    alpha = 0.05   # Np/m -- lossy line
    Z0 = 50.0

    short_stub = stubSolver(real=0, fake=0, z0real=Z0, z0fake=0,
                             beta=beta, alpha=alpha, short=True)
    open_stub = stubSolver(real=0, fake=0, z0real=Z0, z0fake=0,
                            beta=beta, alpha=alpha, short=False)

    target = 30j

    lossy_l, lossless_l, delta = open_stub.required_length(target)
    print(f"Target Zin: {target}")
    print(f"Lossy stub length:     {lossy_l:.5f} m")
    print(f"Lossless stub length:  {lossless_l:.5f} m")
    print(f"Delta (add/remove):    {delta:+.5f} m")

    check = open_stub.input_impedance(length=lossy_l)
    print(f"Check Zin at lossy length: {check}")