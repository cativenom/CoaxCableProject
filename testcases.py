import unittest
import cmath

from solver import Solver
from stubSolver import stubSolver

class testSolver(unittest.TestCase):
    
    def test_rg58(self):
        rg58 = Solver("Copper", "Polyethylene", "Dunno", 0.000405, 0.001475, 1, 1, 1000000000)
        rg58.solve()

        self.assertTrue(abs(rg58.z0.real - 50) < 5)
        self.assertTrue(abs(rg58.z0.imag) < 5)

        rg58_stub = stubSolver(50, 50, rg58.z0.real, rg58.z0.imag, rg58.gamma.real, rg58.gamma.imag, length=0.05)

        Zin = rg58_stub.input_impedance()

        tol = 0.05 * abs(rg58.z0.real)
        self.assertTrue(abs(Zin.real - rg58.z0.real) < tol)
        # self.assertTrue(abs(Zin.imag - rg58.z0.imag) < tol)

    def test_rg59(self):
        rg59 = Solver("Copper", "Polyethylene", "Dunno", 0.00029, 0.00185, 1, 1, 1000000000)
        rg59.solve()

        self.assertTrue(abs(rg59.z0.real - 75) < 5)
        self.assertTrue(abs(rg59.z0.imag) < 5)

        rg59_stub = stubSolver(50, 50, rg59.z0.real, rg59.z0.imag, rg59.gamma.real, rg59.gamma.imag, length=0.05)

        Zin = rg59_stub.input_impedance()

        tol = 0.05 * abs(rg59.z0.real)
        self.assertTrue(abs(Zin.real - rg59.z0.real) < tol)
        # self.assertTrue(abs(Zin.imag - rg59.z0.imag) < tol)

    def test_rg8(self):
        rg8 = Solver("Copper", "Polyethylene", "Dunno", 0.001085, 0.00362, 1, 1, 1000000000)
        rg8.solve()

        self.assertTrue(abs(rg8.z0.real - 50) < 5)
        self.assertTrue(abs(rg8.z0.imag) < 5)

        rg8_stub = stubSolver(50, 50, rg8.z0.real, rg8.z0.imag, rg8.gamma.real, rg8.gamma.imag, length=0.05)

        Zin = rg8_stub.input_impedance()

        tol = 0.05 * abs(rg8.z0.real)
        self.assertTrue(abs(Zin.real - rg8.z0.real) < tol)
        # self.assertTrue(abs(Zin.imag - rg8.z0.imag) < tol)

    def test_rg142(self):
        rg142 = Solver("Copper", "Polyethylene", "Dunno", 0.00047, 0.00151, 1, 1, 1000000000)
        rg142.solve()

        self.assertTrue(abs(rg142.z0.real - 50) < 5)
        self.assertTrue(abs(rg142.z0.imag) < 5)

        rg142_stub = stubSolver(50, 50, rg142.z0.real, rg142.z0.imag, rg142.gamma.real, rg142.gamma.imag, length=0.05)

        Zin = rg142_stub.input_impedance()

        tol = 0.05 * abs(rg142.z0.real)
        self.assertTrue(abs(Zin.real - rg142.z0.real) < tol)
        # self.assertTrue(abs(Zin.imag - rg142.z0.imag) < tol)

    def test_airlossless(self):
        air = Solver("Copper", "Air", "Dunno", 0.0005, 0.0015, 1, 1, 1000000000)
        air.solve()

        self.assertTrue(abs(air.z0.imag) < 5)

        air_stub = stubSolver(50, 50, air.z0.real, air.z0.imag, air.gamma.real, air.gamma.imag, length=0.05)
        
        Zin = air_stub.input_impedance()

        tol = 0.05 * abs(air.z0.real)
        self.assertTrue(abs(Zin.real - air.z0.real) < tol)
        # self.assertTrue(abs(Zin.imag - air.z0.imag) < tol)

if __name__ == '__main__':
    unittest.main()
