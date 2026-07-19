import cmath

class stubSolver:
    def __init__(self, impedance: float, beta: float, gamma: complex,
                 lumpedZ: float, length: float, short: bool):
        self.Z0 = impedance
        self.beta = beta
        self.gamma = gamma if gamma is not None else 1j * beta
        self.lumpedZ = lumpedZ
        self.length = length
        self.short = short

        def _solve_short(gamma, length, Z0):
            return Z0 * cmath.tanh(gamma * length)

        def _solve_open(gamma, length, Z0):
            return Z0 / cmath.tanh(gamma * length)

        self._solve_short = _solve_short
        self._solve_open = _solve_open

    def input_impedance(self):
        if self.short:
            return self._solve_short(self.gamma, self.length, self.Z0)
        else:
            return self._solve_open(self.gamma, self.length, self.Z0)

    def input_reactance(self):
        return self.input_impedance().imag


if __name__ == "__main__":
    beta = 1.0
    length = 0.125
    Z0 = 50.0

    short_stub = stubSolver(impedance=Z0, beta=beta, gamma=1j*beta,
                             lumpedZ=None, length=length, short=True)
    open_stub = stubSolver(impedance=Z0, beta=beta, gamma=1j*beta,
                            lumpedZ=None, length=length, short=False)

    print("Short-circuit stub Zin:", short_stub.input_impedance())
    print("Open-circuit stub Zin:", open_stub.input_impedance())